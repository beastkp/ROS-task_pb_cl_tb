#!/usr/bin/env python

import sys
import rospy
from assign1.srv import compute_ang_vel,compute_ang_velResponse

def callback1():
    float radius
    omega = 0.1/radius
    return compute_ang_velResponse(omega)

def server1():
    rospy.init_node('server1')
    s = rospy.Service('server1',server1,callback1)
    rospy.spin()


if __name__ == '__main__':
    server1()