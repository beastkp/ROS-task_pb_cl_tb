#!/usr/bin/env python
from future import print_function

import rospy
from assign1.srv import compute_ang_vel,compute_ang_velResponse

linearvel = 0.1

def callback1(req):
    print("Requesting service for [%s and %s]"%(req.radius,linearvel))
    print("Angular velocity :%s"%(linearvel/req.radius))
    compute_ang_velResponse(linearvel/req.radius)
    

def service2():
    rospy.init_node("turtlebotserv",anonymous=True)
    s = rospy.Service("compute_ang_vel",compute_ang_vel,callback1)
    rospy.spin()


if __name__ == "__main__":
    service2()