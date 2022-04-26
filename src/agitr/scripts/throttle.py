#!/usr/bin/env python3
# This program generates log messages at varying severity
# levels, throttled to various maximum speeds.
import rospy

rospy.init_node("log_throttled")

while not rospy.is_shutdown():
	rospy.logdebug_throttle(0.1, "This appears every 0.1 seconds.")
	rospy.loginfo_throttle(0.3, "This appears every 0.3 seconds.")
	rospy.logwarn_throttle(0.5, "This appears every 0.5 seconds.")
	rospy.logerr_throttle(1.0, "This appears every 1.0 seconds.")
	rospy.logfatal_throttle(2.0, "This appears every 2.0 seconds.")
