#!/usr/bin/env python3
# This program subscribe to turtle1/pose and shows its 
# messages on the screen.

import rospy
from turtlesim.msg import Pose

# A callback function
# Executed each time a new pose message arrives.
def pose_message_received(msg):
	rospy.loginfo(f"position={msg.x} direction={msg.theta}")
	
# Initialilze the ROS node system and become a node
rospy.init_node("subscribe_to_pose")

# Create a subscriber object
rospy.Subscriber("turtle1/pose", Pose, pose_message_received)

# Let ROS take over
rospy.spin()

