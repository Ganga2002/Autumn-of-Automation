#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('inertia')
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

rate = rospy.Rate(1)

mc_empty = Twist()

mc0 = Twist()
mc0.angular.z = -1.57

mc1 = Twist()
mc1.linear.x = 2.0
mc1.angular.z = 3.14

mc2 = Twist()
mc2.linear.x = 2.0

mc3 = Twist()
mc3.linear.x = -0.5

mc4 = Twist()
mc4.angular.z = 1.57

mc5 = Twist()
mc5.linear.x = 0.5

mc6 = Twist()
mc6.linear.x = 1.5
mc6.angular.z = 3.14


empty = [mc_empty, mc0, mc1, mc2, mc3, mc4, mc5, mc6, mc5]

for i in range(9):
	print(i)
	pub.publish(empty[i])
	rate.sleep()


