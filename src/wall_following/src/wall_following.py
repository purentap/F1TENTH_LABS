#!/usr/bin/env python3
from __future__ import print_function
import sys
import math
import numpy as np
import time 

#ROS Imports
import rospy
from sensor_msgs.msg import Image, LaserScan
from ackermann_msgs.msg import AckermannDriveStamped, AckermannDrive

#PID CONTROL PARAMS
kp = 0.75
kd = 0.01
ki = 0.0001
servo_offset = 0.0
prev_error = 0.0 
error = 0.0
integral = 0.0

#WALL FOLLOW PARAMS
ANGLE_RANGE = 270 # Hokuyo 10LX has 270 degrees scan
DESIRED_DISTANCE_RIGHT = 0.8 # meters
DESIRED_DISTANCE_LEFT = 0.7
VELOCITY = 2.00 # meters per second
CAR_LENGTH = 0.50 # Traxxas Rally is 20 inches or 0.5 meters

class WallFollow:
    """ Implement Wall Following on the car
    """
    def __init__(self):
        #Topics & Subs, Pubs
        lidarscan_topic = '/scan'
        drive_topic = '/nav'
        self.prev_error = 0
        self.prev_time = time.time()
        self.integral = 0
        self.LookaheadDistance =1.5 
        self.lidar_sub = rospy.Subscriber(lidarscan_topic, LaserScan, self.lidar_callback) #Subscribe to LIDAR
        self.drive_pub = rospy.Publisher(drive_topic, AckermannDriveStamped, queue_size=10)#: Publish to drive

    def getRange(self, data, angle):
        # data: single message from topic /scan
        # angle: between -45 to 225 degrees, where 0 degrees is directly to the right
        # Outputs length in meters to object with angle in lidar scan field of view
        #make sure to take care of nans etc.
        #TODO: implement

        starting_angle = data.angle_min #starting angle of the lidar scan, which is -180 degrees
        b_index = int((math.radians(90) - starting_angle) / data.angle_increment)

        angle_rad = math.radians(angle) #upper angle limit for us to find the values inbetween
        a_index= (angle_rad - starting_angle) / data.angle_increment #index of a to obtain from data.ranges
    
        return data.ranges[int(a_index)], data.ranges[int(b_index)]

    def pid_control(self, error, velocity):
        global integral
        global prev_error
        global kp
        global ki
        global kd
        angle = 0.0
        
        current_time = time.time()
        delta_time = current_time - self.prev_time
        self.integral += self.prev_error * delta_time


        angle = -(
            (kp * error) +
            (kd * ((error - self.prev_error) / delta_time)) + 
            (ki * integral)
        )
        self.prev_error = error
        abs_angle = abs(angle)
        if abs_angle >= math.radians(0) and abs_angle <= math.radians(10):
             velocity = 1.5
        elif(abs_angle > math.radians(10) and abs_angle<= math.radians(20)):
             velocity=1.0
        else:
             velocity = 0.5
             
        drive_msg = AckermannDriveStamped()
        drive_msg.header.stamp = rospy.Time.now()
        drive_msg.header.frame_id = "laser"
        drive_msg.drive.steering_angle = angle
        drive_msg.drive.speed = velocity
        self.drive_pub.publish(drive_msg)

    def followLeft(self, data, leftDist):
        #Follow left wall as per the algorithm 
        return DESIRED_DISTANCE_LEFT - leftDist


    def lidar_callback(self, data):
        """ 
        """
        theta= 45
        self.a, self.b = self.getRange(data, theta)
        alpha = math.atan((self.a * math.cos(theta) - self.b)/(self.a * math.sin(theta)))
        dt = self.b * math.cos(alpha) #distance between the left wall and the car lidar
        #print(dt)
        dt1 = dt + self.LookaheadDistance * math.sin(alpha)

        error = self.followLeft(data, dt1)

        #send error to pid_control
        self.pid_control(error, VELOCITY)

def main(args):
    rospy.init_node("WallFollow_node", anonymous=True)
    wf = WallFollow()
    rospy.sleep(0.1)
    rospy.spin()

if __name__=='__main__':
	main(sys.argv)