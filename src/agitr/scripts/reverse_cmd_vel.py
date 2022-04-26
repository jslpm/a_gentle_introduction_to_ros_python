#!/usr/bin/env python3
# This program subscribes to turtle1/cmd_vel and
# republishes on turtle1/cmd_vel_reversed,
# with the signs inverted.
import rospy
from geometry_msgs.msg import Twist

def commandVelocityReceived(msgIn):
	msgOut = Twist()
	msgOut.linear.x = -msgIn.linear.x
	msgOut.angular.z = -msgIn.angular.z
	pub.publish(msgOut)

rospy.init_node("reverse_velocity")
pub = rospy.Publisher("turtle1/cmd_vel_reversed", Twist, queue_size=1000)
sub = rospy.Subscriber("turtle1/cmd_vel", Twist, commandVelocityReceived)

rospy.spin()

