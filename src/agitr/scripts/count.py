#!/usr/bin/env python3
# This program periodically generates log messages at
# various severity levels.
import rospy

rospy.init_node("count_and_log")
rate = rospy.Rate(10);
i = 0

while not rospy.is_shutdown():
	# Generate log messages of varyng severity regularly.
	rospy.logdebug(f"Counted to {i}")
	if (i % 3) == 0:
		rospy.loginfo(f"{i} is divisible by 3.")
	if (i % 5) == 0:
		rospy.logwarn(f"{i} es divisible by 5.")
	if (i % 10) == 0:
		rospy.logerr(f"{i} is divisible by 10.")
	if (i % 20) == 0:
		rospy.logfatal(f"{i} is divisible by 20.")
	# increment
	i += 1 
	rate.sleep()

