#!/usr/bin/env python3

# This program publishes random velocity commands,
# using a maximum linear velocity read from a parameter.
import rospy
import random
from geometry_msgs.msg import Twist

rospy.init_node("publish_velocity")
pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=1000);

# Get the maximum velocity parameter
PARAM_NAME = "~max_vel"
maxVel = None
maxVel = rospy.get_param(PARAM_NAME)
if maxVel is None:
	rospy.logfatal(f"Coud not get parameter {PARAM_NAME}")
	quit()

rate = rospy.Rate(2)
while not rospy.is_shutdown():
	# Create and send a random velocity command.
	msg = Twist()
	msg.linear.x = maxVel * random.random()
	msg.angular.z = random.gauss(0, 1)
	pub.publish(msg)
	
	# Wait until it's time for another iteration
	rate.sleep()
