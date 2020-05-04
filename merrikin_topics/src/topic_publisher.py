#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32 # standard int

# setup: initialize node, register topic, set rate
rospy.init_node( 		# register topic with roscore
	'topic_publisher' 	# node default name
)
pub = rospy.Publisher( 		#register topic with roscore
	'counter', 		# topic name
	Int32, 			# topic type
	queue_size=5 		# queue size
)
rate = rospy.Rate(2) 		# adaptive rate in Hz

# Loop: publish, count, sleep
count = 0
while not rospy.is_shutdown():
	pub.publish(count) 	# piublish count
	count += 1 		# increment
	rate.sleep() 		# set by rospy.Rate above
