#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
   
    while not rospy.is_shutdown():
        hello = "Welcome to ROS world %s' % rospy.get_time()
        rospy.loginfo(hello)
        pub.publish(hello)
        rate.sleep()


if __name__ == '__main__':
    try:
        talk()
    except rospy.ROSInterruptException:
        pass
