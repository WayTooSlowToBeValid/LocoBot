#! /usr/bin/env python3

import rospy
import time
rospy.init_node('ObiWan')


print ("Help me Obi-Wan Kenobi, you're my only hope")
for i in range(10):
	print(10-i)
	time.sleep(1)
