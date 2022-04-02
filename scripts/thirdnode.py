#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback1(data):
    rospy.loginfo("%s",data.data)
def callback2(data):
    rospy.loginfo("%s",data.data)
def thirdnode():
    rospy.init_node('thirdnode', anonymous=True)
    rospy.Subscriber("/hello",String,callback1)
    rospy.Subscriber("/world",String,callback2)
    rospy.spin()

if __name__ == '__main__':
  thirdnode()