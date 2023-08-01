#!/usr/bin/env python3
from __future__ import print_function
import sys
import math
from scipy.ndimage import uniform_filter1d
import numpy as np

#ROS Imports
import rospy
from sensor_msgs.msg import Image, LaserScan
from ackermann_msgs.msg import AckermannDriveStamped, AckermannDrive

class reactive_follow_gap:
    def __init__(self):
        #Topics & Subscriptions,Publishers
        lidarscan_topic = '/scan'
        drive_topic = '/nav'

        self.lidar_sub = rospy.Subscriber(lidarscan_topic, LaserScan, self.lidar_callback)
        self.drive_pub = rospy.Publisher(drive_topic, AckermannDriveStamped, queue_size = 10)
    
    def preprocess_lidar(self, ranges,range_min, range_max):
        """ Preprocess the LiDAR scan array. Expert implementation includes:
            1.Setting each value to the mean over some window
            2.Rejecting high values (eg. > 3m)
        """
        proc_ranges = uniform_filter1d(ranges, size=5)
        #proc_ranges = np.clip(proc_ranges, a_min=range_min, a_max=7.0)

        for i in range(self.start_idx, self.end_idx+1):
            if math.isnan(proc_ranges[i] or math.isinf(proc_ranges[i])):
                proc_ranges[i] = 0.0
            elif proc_ranges[i] > range_max:
                proc_ranges[i] = range_max

        return proc_ranges
    
    def find_max_gap(self, free_space_ranges):
        """ Return the start index & end index of the max gap in free_space_ranges
        """
        temp = []
        max_gap_sequence = []
        inSameSeq = False
        curr_start_idx = -1
        start_idx = -1
        end_idx= -1
  
        for i in range(self.start_idx, self.end_idx+1):

            if free_space_ranges[i] > 1.5:
                temp.append(free_space_ranges[i])
                if inSameSeq is False:
                    curr_start_idx = i
                    inSameSeq = True

                if i == self.end_idx:
                    if((len(temp) >= len(max_gap_sequence)) and (len(temp) != 0)):
                        max_gap_sequence = temp
                        inSameSeq = False
                        end_idx = i-1
                        start_idx = curr_start_idx
            else:
                if((len(temp) >= len(max_gap_sequence)) and (len(temp) != 0)):
                    max_gap_sequence = temp
                    inSameSeq = False
                    end_idx = i-1
                    start_idx = curr_start_idx
                temp =[]

        '''
        if start_idx== -1 or end_idx == -1 :
            print("ARRAY LEN IS 0; ")
            print("curr start index is: ", curr_start_idx)
            for i in range(self.start_idx, self.end_idx+1):
                print(free_space_ranges[i])
        '''
        return max_gap_sequence, start_idx, end_idx
    
        
    def find_closest_point(self, start_i, end_i, ranges):

        #best_point_idx = np.argmin(ranges[start_i:end_i+1])
        close_points = 5
        current_min = self.range_max *close_points + 1

        min_point_idx = -1
        for i in range(start_i, end_i+1):
            
            distance = ranges[i-2] + ranges[i-1] + ranges[i] + ranges[i+1] + ranges[i+2]
            if(distance < current_min):
                current_min = distance
                min_point_idx = i
        return min_point_idx
    
    def find_best_point(self, start_i, end_i, ranges):
        """Start_i & end_i are start and end indicies of max-gap range, respectively
        Return index of best point in ranges
    Naive: Choose the furthest point within ranges and go there
        """
        best_point_idx = np.argmin(ranges[start_i:end_i+1])
        return best_point_idx

    def lidar_callback(self, data):
        """ Process each LiDAR scan as per the Follow Gap algorithm & publish an AckermannDriveStamped Message
        """
        #angle_min = data.range_min
        self.range_max = data.range_max
        lidar_angle_min = data.angle_min
        ranges = data.ranges

        angle_inc = data.angle_increment
        self.start_idx = int(math.radians(110) / angle_inc)
        self.end_idx = int(math.radians(250) / angle_inc)
        
        #min_angle = (-70 / 180.0) * math.pi
        #max_angle = 70/180 * math.pi
        #max_index = int((max_angle - lidar_angle_min)/ angle_inc)
        #self.start_idx = int((min_angle - lidar_angle_min) /angle_inc)

        proc_ranges = self.preprocess_lidar(ranges, data.range_min, data.range_max)

        #Find closest point to LiDAR
        closest_point_idx = self.find_closest_point(self.start_idx, self.end_idx, proc_ranges)
        #Eliminate all points inside 'bubble' (set them to zero) 
        bubble_radius = 150 #radius of the bubble
        len_ranges = len(proc_ranges)

        proc_ranges[closest_point_idx] = 0

        for i in range(1, bubble_radius+1):
            if closest_point_idx+i < len_ranges:
                proc_ranges[closest_point_idx+i] = 0
            if 0<= closest_point_idx-i:
                proc_ranges[closest_point_idx-i]=0
        
        #Find max length gap 
        max_gap_list,start_idx, end_idx = self.find_max_gap(proc_ranges)

        #print(start_idx, end_idx)
        #Find the best point in the gap 
        
        if(len(proc_ranges[start_idx:end_idx]) == 0):
            
            print("ARRAY LEN IS 0; START INDEX:", start_idx, "END INDEX: ", end_idx)
            #print("**********************************************************************************************")
        else:
            best_point_idx = np.argmax(proc_ranges[start_idx:end_idx]) + self.start_idx
            current_max = 0.0
            for i in range(start_idx, end_idx+1):
                if(proc_ranges[i] > current_max):
                    current_max = proc_ranges[i]
                    max_index = i 
                    max_angle = (max_index * angle_inc) + lidar_angle_min  
                elif(proc_ranges[i] == current_max):
                    max_angle = (i * angle_inc) + lidar_angle_min



            #print("#OF ELMS BIGGER TAN 0.7: ", list(proc_ranges[start_idx:end_idx]).count(0.3)+ list(proc_ranges[start_idx:end_idx]).count(0.2)+ list(proc_ranges[start_idx:end_idx]).count(0.1)+ list(proc_ranges[start_idx:end_idx]).count(0.0))
            #print("LEN", len(max_gap_list))
            best_point_angle = (best_point_idx * angle_inc) + lidar_angle_min

            abs_angle = abs(max_angle)
            if abs_angle >= math.radians(0) and abs_angle <= math.radians(10):
                    velocity = 1.5
            elif(abs_angle > math.radians(10) and abs_angle<= math.radians(20)):
                    velocity=1.0
            else:
                    velocity = 0.5
            #Publish Drive message
            drive_msg = AckermannDriveStamped()
            drive_msg.header.stamp = rospy.Time.now()
            drive_msg.header.frame_id = "laser"
            drive_msg.drive.steering_angle = max_angle
            drive_msg.drive.speed = velocity
            self.drive_pub.publish(drive_msg)
        
def main(args):
    rospy.init_node("FollowGap_node", anonymous=True)
    rfgs = reactive_follow_gap()
    rospy.sleep(0.1)
    rospy.spin()

if __name__ == '__main__':
    main(sys.argv)