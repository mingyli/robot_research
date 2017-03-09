
import rospy
import baxter_interface
from baxter_interface import Gripper
import tf
from sensor_msgs.msg import PointCloud


rospy.init_node('Quickstart')
right = baxter_interface.Limb('right')
left = baxter_interface.Limb('left')

right_gripper = Gripper('right')
left_gripper = Gripper('left')

def callback(data):
	# print data
	print listener.transformPointCloud('/left_lower_forearm', data)

#start the listener
listener = tf.TransformListener()
rospy.Subscriber('mocap_point_cloud', PointCloud, callback)
rospy.spin()
# rospy.sleep(2) # waits for data to be published to topic. tf will grab last-published position

# while True:
# 	raw_input("Press Enter for transform coords")
# 	while True:
# 		try:
# 			# (trans,rot) = listener.lookupTransform('/right_gripper', '/base', rospy.Time(0))
# 			# Look up the position of the right gripper w.r.t. base
# 			# ((x, y, z), (x, y, z, w))
# 			# angles = right.joint_angles()
			
# 			break
# 		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
# 		    continue
# 	print((trans, rot))
# 	print angles
