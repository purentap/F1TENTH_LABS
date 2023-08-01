#!/usr/bin/env python3
import rospy
import numpy as np
import atexit
import tf
import math 
from os.path import expanduser
from time import gmtime, strftime
from numpy import linalg as LA
from tf.transformations import euler_from_quaternion
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point

home = expanduser('~')

class WaypointLogger(object):
    """
    The class that handles recording waypoints
    """

    def __init__(self):
        self.MIN_DISTANCE = 0.15
        self.MIN_VELOCITY = 0.0  # m/s
        self.waypoints_dir = "~/testcar/testcar_ws/waypoints/wp-%Y-%m-%d-%H-%M-%S"

        self.home = expanduser('~')
        self.file = open(strftime(home+'/ros_workspaces/f1tenth_labs/lab1/logs/wp-%Y-%m-%d-%H-%M-%S',gmtime())+'.csv', 'w')
        self.cache = {}

        rospy.Subscriber("/pf/pose/odom", Odometry, self.save_waypoint)

    def save_waypoint(self, data):
        
        lastwaypoint = self.cache['lp'] if 'lp' in self.cache else self.cache.setdefault('lp', data.pose.pose.position) 
        quaternion = np.array([data.pose.pose.orientation.x, 
                            data.pose.pose.orientation.y, 
                            data.pose.pose.orientation.z, 
                            data.pose.pose.orientation.w])

        euler = tf.transformations.euler_from_quaternion(quaternion)
        speed = LA.norm(np.array([data.twist.twist.linear.x, 
                                data.twist.twist.linear.y, 
                                data.twist.twist.linear.z]),2)

        #if data.twist.twist.linear.x>0.0:
        #    print data.twist.twist.linear.x

        dist = 0.0
        dx = data.pose.pose.position.x - lastwaypoint.x
        dy = data.pose.pose.position.y - lastwaypoint.y
        dist = math.sqrt(dx*dx + dy*dy)
        
        if dist >= self.MIN_DISTANCE:
            self.cache['lp'] = data.pose.pose.position
            self.file.write('%f, %f, %f, %f\n' % (data.pose.pose.position.x,
                                        data.pose.pose.position.y,
                                        euler[2],
                                        speed))
    def cleanup(self):
        self.file.close()
        print('Goodbye')

def main():
    rospy.init_node('waypoint_logger', anonymous=True)
    C = WaypointLogger()
    r = rospy.Rate(40)

    while not rospy.is_shutdown():
        C.send_command()
        r.sleep()
    
    C.cleanup()



if __name__ == '__main__':
    main()
