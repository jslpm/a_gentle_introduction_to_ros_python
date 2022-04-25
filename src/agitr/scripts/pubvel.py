#!/usr/bin/env python3

# This program publishes randomly-generated velocity
# messages for turtlesim.
import rospy
import random
from geometry_msgs.msg import Twist

# initialize the ROS system and become a node.
rospy.init_node("publish_velocity");

# Create a publisher object.
pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=1000);

# Seed the random number generator.
random.seed(0)

# Loop at 2 Hz until the node is shutdown.
rate = rospy.Rate(2)
while not rospy.is_shutdown():
	# Create and fill in the message.
	# The other four fields, which are ignored by turtlesim,
	# default to 0.
	msg = Twist()
	msg.linear.x = random.random()
	msg.angular.z = random.gauss(0, 1)
	
	# Publish the message.
	pub.publish(msg)
	
	# Send a message to rosout with the details.
	rospy.loginfo(f"Sending random velocity command: linear={msg.linear.x} angular={msg.angular.z}")
	
	# Wait until it's time for another iteration.
	rate.sleep()

