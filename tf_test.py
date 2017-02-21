import rospy
import baxter_interface
from baxter_interface import Gripper
import tf


rospy.init_node('Quickstart')
right = baxter_interface.Limb('right')
left = baxter_interface.Limb('left')

right_gripper = Gripper('right')
left_gripper = Gripper('left')

listener = tf.TransformListener()
rospy.sleep(2) # waits for data to be published to topic. tf will grab last-published position

while True:
	try:
		(trans,rot) = listener.lookupTransform('/right_gripper', '/base', rospy.Time(0))
		# ((x, y, z), (x, y, z, w))
		break
	except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
	    continue

print(trans, rot)