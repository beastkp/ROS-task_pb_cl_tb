#!/usr/bin/env python
import rospy 
from std_msgs.msg import String

def World():
    pub = rospy.Publisher('/world', String, queue_size=10)
    rospy.init_node("World", anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        world_str = "World !"
        rospy.loginfo(world_str)
        pub.publish(world_str)
        rate.sleep()

if __name__ == '__main__':
    try:
         World()
    except rospy.ROSInterruptException:
        pass
    
        