#!/usr/bin/env python3
# This program generates a single log message at each
# severity level
import rospy

rospy.init_node("log_once")

while not rospy.is_shutdown():
	rospy.logdebug_once("This appears only once.")
	rospy.loginfo_once("This appears only once.")
	rospy.logwarn_once("This appears only once.")
	rospy.logerr_once("This appears only once.")
	rospy.logfatal_once("This appears only once.")
