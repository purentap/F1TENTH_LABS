#!/usr/bin/env python3
import rospy
import csv
import numpy as np
import math
import time
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped, Point
from sensor_msgs.msg import LaserScan
from visualization_msgs.msg import MarkerArray, Marker
from ackermann_msgs.msg import AckermannDriveStamped
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from numpy import linalg as la



# TODO: import ROS msg types and libraries

class PurePursuit(object):
    """
    The class that handles pure pursuit.
    """
    def __init__(self):
        #waypoints_csv_loc = rospy.get_param("waypoint_csv_loc")
        waypoints_csv_loc = "/home/puren/ros_workspaces/f1tenth_labs/lab1/logs/wp-2023-07-27-09-50-45.csv"
        self.waypoints = self.get_waypoints_from_csv(waypoints_csv_loc)

        #self.L = rospy.get_param("L") #Lookahead distance
        self.L = 1.0

        # TODO: create ROS subscribers and publishers.
        self.initial_pos_sub = rospy.Subscriber("/pf/viz/inferred_pose", PoseStamped, callback=self.pose_callback)

        self.drive_pub = rospy.Publisher("/drive", AckermannDriveStamped, queue_size=10)

        self.marker_pub = rospy.Publisher("/visualization_marker", Marker, queue_size=100 )
        self.goal_idx = 0 
    def publish_marker(self, goal):
        marker = Marker()
        marker.id = -2
        marker.header.frame_id = "map"
        marker.type = Marker.CUBE
        marker.action = Marker.ADD
        marker.pose.position.x = goal[0]
        marker.pose.position.y = goal[1]
        marker.pose.position.z = 0.0
        marker.pose.orientation.x = 0.0
        marker.pose.orientation.y = 0.0
        marker.pose.orientation.z = 0.0
        marker.pose.orientation.w = 1.0
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2
        marker.color.a = 1.0
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 1.0
        self.marker_pub.publish(marker)

    def get_waypoints_from_csv(self, file_loc):
        file = open(file_loc)
        csvreader = csv.reader(file)
        waypoints = []

        for row in csvreader:
            print(row)
            waypoints.append(row)
        print(len(waypoints))
        return waypoints
    '''
    def visualize_waypoints(self):
        visualize_pub = rospy.Publisher("visualization_marker_array", MarkerArray, queue_size=100)
        waypoints_locs = [[float(waypoint[0]), float(waypoint[1])] for waypoint in self.waypoints]

        print(waypoints_locs)
        marker_array = MarkerArray()

        
        for i in range(len(waypoints_locs)):
            wp = waypoints_locs[i]
            
            marker = Marker()


            marker.header.frame_id = "map"

            marker.header.stamp = time.time()

            marker.type = marker.CUBE
            marker.id = i

            marker.action = marker.ADD
            marker.lifetime = rospy.Duration()

            # Set the scale of the marker
            marker.scale.x = 1.0
            marker.scale.y = 1.0
            marker.scale.z = 0.0

            # Set the color
            marker.color.r = 1.0
            marker.color.g = 0.0
            marker.color.b = 1.0
            marker.color.a = 1.0

            marker.pose.orientation.x = 0.0
            marker.pose.orientation.y = 0.0
            marker.pose.orientation.z = 0.0
            marker.pose.orientation.w = 1.0 

            marker.pose.position.x = wp[0]
            marker.pose.position.y = wp[1]
            marker.pose.position.z = 0.0


            marker_array.markers.append(marker)

            visualize_pub.publish(marker_array)
        rospy.sleep(5)
        '''
    def get_lookahead_waypoint(self):
        #math.dist(self.initial_pose.pose.pose.position)
        current_2d_loc = [self.current_x,  self.current_y]
        waypoints_locs = [[float(waypoint[0]), float(waypoint[1])] for waypoint in self.waypoints]
        rate = 0.2
        look_ahead_pts = [] #waypoints where distance between the current pos >= L-rate and current_pos <= L + rate
        for idx, wp in enumerate(waypoints_locs):

            if math.dist(current_2d_loc, wp) >= self.L - rate and math.dist(current_2d_loc, wp) <= self.L+rate:
                 look_ahead_pts.append((idx, self.waypoints[idx]))
        #print(math.dist(current_2d_loc,waypoints_locs[min_distance_wp_idx]))
        return look_ahead_pts

    # find the angle bewtween two vectors
    def find_angle(self, v1, v2):
        cosang = np.dot(v1, v2)
        sinang = la.norm(np.cross(v1, v2))
        return np.arctan2(sinang, cosang)
    def calculate_steering_angle(self, L, y):
        return (2 * y) / (math.pow(L, 2))

    def pose_callback(self, pose_msg):
        # TODO: find the current waypoint to track using methods mentioned in lecture
        self.current_pos = pose_msg
        self.current_x = float(pose_msg.pose.position.x)
        self.current_y = float(pose_msg.pose.position.y)

        
        qx = self.current_pos.pose.orientation.x
        qy = self.current_pos.pose.orientation.y
        qz = self.current_pos.pose.orientation.z
        qw = self.current_pos.pose.orientation.w

        quaternion = [qx,qy,qz,qw]
        roll, pitch, yaw = euler_from_quaternion(quaternion)

        #print(roll, pitch, yaw)
        close_waypoints = self.get_lookahead_waypoint()

        
        for i, wp in enumerate(close_waypoints):

            v1 = [float(wp[1][0]) - self.current_x, float(wp[1][1]) - self.current_y]
            v2 = [np.cos(yaw), np.sin(yaw)]
            
            temp_angle = self.find_angle(v1, v2)

            if abs(temp_angle) < np.pi/2:
                self.goal_idx = wp[0]
                break

        goal_pt = self.waypoints[self.goal_idx]

        goal_x , goal_y, goal_w = float(goal_pt[0]) , float(goal_pt[1]), float(goal_pt[2])

        # TODO: transform goal point to vehicle frame of reference 
        gvcx = goal_x - self.current_x
        gvcy= goal_y - self.current_y

        goal_x_veh_coord = gvcx * np.cos(yaw) + gvcy* np.sin(yaw)
        goal_y_veh_coord = gvcy*np.cos(yaw) - gvcx*np.sin(yaw)

        self.publish_marker([goal_x, goal_y])

        # TODO: calculate curvature/steering angle

        #k = 2 * math.sin(alpha)/self.L
        #angle_i = math.atan(k*self.L)
        #angle = angle_i*2
        
        # sin(yaw) * cos(pitch)
        siny_cosp = 2.0 * (
            quaternion[3] * quaternion[2] + quaternion[0] * quaternion[1]
        )

        # cos(yaw) * cos(pitch)
        cosy_cosp = 1.0 - 2.0 * (
            quaternion[1] * quaternion[1] + quaternion[2] * quaternion[2]
        )
        heading_current = np.arctan2(siny_cosp, cosy_cosp)

        # Calculating the Euclidean distance between the vehicle and the goal waypoint
        euclidean_dist = math.dist([goal_x, goal_y], [self.current_x, self.current_y])

        # Calculating the lookahead angle between the vehicle and the goal waypoint
        lookahead_angle = np.arctan2(goal_y - self.current_y, goal_x- self.current_x)

        # Calculating the cross-track error (the lateral distance between the vehicle's current position and the line defined by the goal waypoint and the vehicle's heading)
        delta_y = euclidean_dist * np.sin(lookahead_angle - heading_current)

        steering_angle = self.calculate_steering_angle(self.L, delta_y)


        # TODO: publish drive message, don't forget to limit the steering angle between -0.4189 and 0.4189 radians
        
        if(steering_angle> 0.4189): steering_angle = 0.4189
        elif (steering_angle < -0.4189): steering_angle = -0.4189


        abs_angle = abs(steering_angle)
        velocity = 2.0
        if abs_angle >= math.radians(0) and abs_angle <= math.radians(10):
                velocity = 1.5
        elif(abs_angle > math.radians(10) and abs_angle<= math.radians(20)):
                velocity=1.0
        else:
                velocity = 0.5
        drive_msg = AckermannDriveStamped()
        drive_msg.header.stamp = rospy.Time.now()
        drive_msg.header.frame_id = "base_link"
        drive_msg.drive.steering_angle = steering_angle
        drive_msg.drive.steering_angle_velocity = 1
        drive_msg.drive.speed = velocity
        drive_msg.drive.acceleration = 1
        drive_msg.drive.acceleration = 1

        self.drive_pub.publish(drive_msg)
        

def main():
    rospy.init_node('pure_pursuit_node')
    pp = PurePursuit()
    rospy.spin()
if __name__ == '__main__':
    main()