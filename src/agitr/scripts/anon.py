#!/usr/bin/env python3

# This program starts with an anonymous name, which
# allows multiple copies to excecute at the same time,
# without needing to manually create distinct name
# for each of them
import rospy

rospy.init_node("anon", anonymous=True)
rate = rospy.Rate(1);
while not rospy.is_shutdown():
	rospy.loginfo(f"This message is from {rospy.get_name()}")
	rate.sleep()
