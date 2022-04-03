#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String 
from assign1.srv import *

radius = 5
def callback1():
    while not rospy.is_shutdown():
        try:
            computeangvel = rospy.ServiceProxy('compute_ang_vel',compute_ang_vel)
            resp1 = computeangvel(int(radius))
            return resp1.angvel
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)
pub = rospy.Publisher("cmd_vel",Twist,queue_size=1)


def turtlebotsub():
    rospy.init_node('turtlebotsub')
    rospy.Subscriber("\radius",String, callback1)
    rospy.spin()
    rospy.wait_for_service('compute_ang_vel')
        
if __name__ == '__main__':
    turtlebotsub()
