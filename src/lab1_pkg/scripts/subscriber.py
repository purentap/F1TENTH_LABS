#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan
from lab1_pkg.msg import scan_range
import numpy as np

#pub_closest = rospy.Publisher('/closest_point' , scan_range, queue_size=10)
#pub_farthest = rospy.Publisher('/farthest_point', scan_range, queue_size=10)
pub_scan_range = rospy.Publisher('/scan_range', scan_range, queue_size=10)
def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "GOT MESSAGE", data)
    if True not in np.isinf(data.ranges) and True not in np.isnan(data.ranges):
        #print(data.ranges[0])
        close_pt = min(data.ranges)
        farthest_pt = max(data.ranges)

        msg = scan_range()
        msg.max_range= farthest_pt
        msg.min_range= close_pt


        #pub_closest.publish(close_pt)
        #pub_farthest.publish(farthest_pt)
        pub_scan_range.publish(msg)

def listener():
    rospy.init_node('listener', anonymous=True)
    sub= rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()

if __name__=='__main__':
    listener()
