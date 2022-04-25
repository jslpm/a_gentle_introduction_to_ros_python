#!/usr/bin/env python3
import rospy

# Initialize the ROS system
rospy.init_node("hello_ros")
# Send some output as a long message
rospy.loginfo("Hello ROS!")

