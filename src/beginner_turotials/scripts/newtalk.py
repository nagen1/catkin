#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('newtopic')
pub = rospy.Publisher('chatter',  String)

while not rospy.is_shutdown():
    pub.publish("Welcome")

