#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def turtlebotpub():
    pubrad = rospy.Publisher('/radius', String ,queue_size=10)    
    rospy.init_node("turtlebotpub",anonymous = True)
    msg1 = String()
    msg1.data="5"
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pubrad.publish(msg1)
        rate.sleep()

if __name__ == '__main__':
    try:
        turtlebotpub()
    except rospy.ROSInterruptException():
        pass