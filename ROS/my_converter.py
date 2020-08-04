#!/usr/bin/env python

import rospy
from final.msg import euler 
from final.msg import quaternion
import math

rospy.init_node('my_converter', anonymous=True)

pub = rospy.Publisher('topic1', quaternion)

pub1 = quaternion()
#input_for_quaternions
pub1.x = input('x-cordinate > ')
pub1.y = input('y-cordinate > ')
pub1.z = input('z-cordinate > ')
pub1.w = input('w-cordinate > ')

rospy.loginfo(pub1)
pub.publish(pub1)

### subscriber1 ###
rec1 = quaternion()

def callback(data):
	global rec1
	rec1 = data.data

sub1 = rospy.Subscriber('topic1', quaternion, callback)

euler_angles = euler()
#conversion_to_euler-angles
while not rospy.is_shutdown():
	# roll (x-axis rotation)	
	sinr_cosp = 2 * (rec1.w * rec1.x + rec1.y * rec1.z)
	cosr_cosp = 1 - 2 * (rec1.x * rec1.x + rec1.y * rec1.y)
	roll = math.degrees(math.atan2(sinr_cosp, cosr_cosp))
	
	# pitch (y-axis rotation)
	sinp = 2.0 * (rec1.w * rec1.y - rec1.z * rec1.x)
        sinp = 1.0 if sinp > 1.0 else sinp
        sinp = -1.0 if sinp < -1.0 else sinp
        pitch = math.degrees(math.asin(sinp))
	
	# yaw (z-axis rotation)
	siny_cosp = 2.0 * (rec1.w * rec1.z + rec1.x * rec1.y)
	cosy_cosp = 1.0 - 2.0 * (rec1.y * rec1.y + rec1.z * rec1.z)
	yaw = math.atan2(siny_cosp, cosy_cosp)

euler_angles = [roll, pitch, yaw]

pub2 = rospy.Publisher('topic2', euler)

