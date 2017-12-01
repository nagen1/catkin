#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('talker')
pub = rospy.Publisher('talker_topic', String)

rate = rospy.Rate(2)

while not rospy.is_shutdown():
    pub.publish("Welcome to ROS")
    rate.sleep()
