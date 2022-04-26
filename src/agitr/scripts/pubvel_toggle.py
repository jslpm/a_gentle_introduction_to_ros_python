#!/usr/bin/env python3

# This program toggles between rotation and translation
# commands based on calls to a service.
import rospy
from std_srvs.srv import Empty
from geometry_msgs.msg import Twist

forward = True

def toggleForward(req):
	global forward
	forward = not forward
	if forward:
		print("Now sending forward commands.")
	else:
		print("Now sending rotate commands.")


rospy.init_node("pubvel_toggle")

# Register our service with the master
server = rospy.Service("toggle_forward", Empty, toggleForward)

# Publish commands using the latest value for forward,
# until the node shuts down.
pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=1000)
rate = rospy.Rate(2)
while not rospy.is_shutdown():
	msg = Twist()
	if forward:
		msg.linear.x = 1.0
		msg.angular.z = 0.0
	else:
		msg.linear.x = 0.0
		msg.angular.z = 1.0
	pub.publish(msg)
	rate.sleep()
