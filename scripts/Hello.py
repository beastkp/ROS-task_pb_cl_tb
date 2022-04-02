#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def Hello():
    pub = rospy.Publisher('/hello', String, queue_size=10)
    rospy.init_node("Hello")
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        hello_str = "Hello,"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        Hello()
    except rospy.ROSInterruptException:
        pass