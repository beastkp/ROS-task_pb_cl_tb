#!/usr/bin/env python

from __future__ import print_function
import sys
# import loggingsetup
import rospy
from matplotlib import pyplot as plt
from assign1.srv import *


def stateclient(x, y, vx, vy):
    rospy.wait_for_service('stateservice')
    while not rospy.is_shutdown():
        try:
            coordinates = rospy.ServiceProxy('stateservice', stateservice)
            # in service proxy use same name used in servie node  and then srv file
            resp1 = coordinates(x, y, vx, vy)
            traj = resp1.xi + resp1.yi
            return traj
        except rospy.ServiceException as e:
            print("Service called failed %s" %e)


if __name__ == '__main__':
    if len(sys.argv) == 5:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        vx = int(sys.argv[3])
        vy = int(sys.argv[4])
    else:
        # print(usage())
        sys.exit(1)

    print("Requesting %s-%s %s-%s" % (x, vx, y, vy))

    print((x, y, stateclient(x, y, vx, vy)))
    # q=(x, y, stateclient(x, y, vx, vy)[1])[2]

    # plt.plot(x, y, label='Point')
    # plt.plot(vx, vy, label='Velocity')
    # plt.plot(stateclient(x, y, vx, vy), label='trajectory')
    # plt.savefig('myplot.png')
