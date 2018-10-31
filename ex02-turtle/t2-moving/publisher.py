#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist


def talker():
	rospy.init_node('controle')

	pub  = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	rate = rospy.Rate(10)
	vel_msg = Twist()

	while not rospy.is_shutdown():
		vel_msg.linear.x = 0.5
		vel_msg.linear.y = 0
		vel_msg.linear.z = 0
		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
		vel_msg.angular.z = 0

		pub.publish(vel_msg)
		rate.sleep()


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
