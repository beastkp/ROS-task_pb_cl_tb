#!/usr/bin/env python
import rospy
from assign1.srv import *

radius = 5
def callback1():
    radius = int(data.data)
    while not rospy.is_shutdown():
        computeangvel = rospy.ServiceProxy('compute_ang_vel',compute_ang_vel)
        rospy.Publisher("cmd_vel",float ,queue_size=10)


def turtlebotsub():
    rospy.init_node('turtlebotsub')
    rospy.Subscriber("\radius",int, callback1)
    rospy.wait_for_service('compute_ang_vel')
        
if __name__ == '__main__':
    turtlebotsub()