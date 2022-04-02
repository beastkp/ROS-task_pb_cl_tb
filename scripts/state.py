#!/usr/bin/env python

from __future__ import print_function
import rospy
from assign1.srv import stateservice, stateserviceResponse


def callback(req):
    print("Requesting Service")
    while not rospy.is_shutdown():
        print("Returning [%s-%s]"%(req.x*req.vx,req.y*req.vy))
        return stateserviceResponse(req.x*req.vx, req.y*req.vx)


def respond():
    rospy.init_node('state')
    s = rospy.Service('stateservice', stateservice, callback)
    rospy.spin()


if __name__ == '__main__':
    print("Starting server node:")
    respond()
