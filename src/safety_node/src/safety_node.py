#!/usr/bin/env python3
import rospy

# TODO: import ROS msg types and libraries
from std_msgs.msg import Bool
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from ackermann_msgs.msg import AckermannDriveStamped
import numpy as np
import math

class Safety(object):
    """
    The class that handles emergency braking.
    """
    def __init__(self):
        """

        One publisher should publish to the /brake topic with a AckermannDriveStamped brake message.

        One publisher should publish to the /brake_bool topic with a Bool message.

        You should also subscribe to the /scan topic to get the LaserScan messages and
        the /odom topic to get the current speed of the vehicle.

        The subscribers should use the provided odom_callback and scan_callback as callback methods

        NOTE that the x component of the linear velocity in odom is the speed
        """
        self.speed = 0
        self.emergency_brake = False
        # TODO: create ROS subscribers and publishers.
        self.brake_publisher = rospy.Publisher('/brake', AckermannDriveStamped, queue_size=10)
        self.brake_bool_publisher = rospy.Publisher('/brake_bool', Bool, queue_size=10)

        self.scan_sub= rospy.Subscriber('/scan', LaserScan, self.scan_callback)
        self.odom_sub = rospy.Subscriber('/odom', Odometry, self.odom_callback)
    def odom_callback(self, odom_msg):
        # TODO: update current speed
        self.speed = odom_msg.twist.twist.linear.x #not sure?

    def scan_callback(self, scan_msg):
        # TODO: calculate TTC
        ranges = scan_msg.ranges
        min_range = scan_msg.range_min
        max_range = scan_msg.range_max

        angle_min = scan_msg.angle_min
        angle_max = scan_msg.angle_max
        angle_increment = scan_msg.angle_increment

        for idx,range in enumerate(ranges):
            if np.isnan(range) or range>max_range or range < min_range:
                continue

            angle = angle_min + (idx * angle_increment)
            ttc = range/ max(math.cos(angle) * self.speed, 0.01)
            if(ttc <2):
                self.emergency_brake = True
                break
        
        emergency_msg = Bool()
        emergency_msg.data = self.emergency_brake
        self.brake_bool_publisher.publish(emergency_msg)

        if(self.emergency_brake):
            brake_msg = AckermannDriveStamped()
            brake_msg.drive.speed = 0.0
            brake_msg.drive.steering_angle = 0.0
            self.brake_publisher.publish(brake_msg)

        else:
            self.emergency_brake = False        

        # TODO: publish brake message and publish controller bool



def main():
    rospy.init_node('safety_node')
    sn = Safety()
    rospy.spin()
    sn.destroy_node()
    rospy.shutdown()

if __name__ == '__main__':
    main()