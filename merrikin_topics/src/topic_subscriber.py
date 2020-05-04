#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(msg): 			# callback for recieving messages
	print(msg.data) 		# print to Terminal

rospy.init_node('topic_subscriber') 	# initialize node
sub = rospy.Subscriber('counter', Int32, callback) # subscribe

rospy.spin() 				#wait for the node to be shut down
