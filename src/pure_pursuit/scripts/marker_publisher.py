#!/usr/bin/env python3

import rospy
import csv
import numpy as np

from visualization_msgs.msg import MarkerArray, Marker



def get_waypoints_from_csv(file_loc):
    file = open(file_loc)
    csvreader = csv.reader(file)
    waypoints = []

    for row in csvreader:
        waypoints.append(row)

    return waypoints
def visualize_waypoints(waypoints):
        waypoints_locs = [[float(waypoint[0]), float(waypoint[1])] for waypoint in waypoints]

        marker_array = MarkerArray()

        
        for i in range(len(waypoints_locs)):
            wp = waypoints_locs[i]
            
            marker = Marker()


            marker.header.frame_id = "map"

            marker.header.stamp = rospy.Time()

            marker.type = marker.SPHERE
            marker.id = i

            marker.action = marker.ADD
            marker.lifetime = rospy.Duration()

            # Set the scale of the marker
            marker.scale.x = 0.1
            marker.scale.y = 0.1
            marker.scale.z = 0.0

            # Set the color
            marker.color.r = 0.0
            marker.color.g = 1.0
            marker.color.b = 0.0
            marker.color.a = 1.0

            marker.pose.orientation.x = 0.0
            marker.pose.orientation.y = 0.0
            marker.pose.orientation.z = 0.0
            marker.pose.orientation.w = 1.0 

            marker.pose.position.x = wp[0]
            marker.pose.position.y = wp[1]
            marker.pose.position.z = 0.0


            marker_array.markers.append(marker)

        return marker_array
def main():     
    rospy.init_node("marker_publisher")
    visualize_pub = rospy.Publisher("/visualization_marker_array", MarkerArray, queue_size=100)

    csv_loc = "/home/puren/ros_workspaces/f1tenth_labs/lab1/logs/wp-2023-07-27-09-50-45.csv"
    
    waypoints = get_waypoints_from_csv(csv_loc)

    marker_array = visualize_waypoints(waypoints)

    print(marker_array)
    
    visualize_pub.publish(marker_array)
    rospy.spin()


if __name__ == '__main__':
    main()