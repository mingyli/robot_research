
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg 
import geometry_msgs.msg
import baxter_interface
from baxter_interface import Gripper
import tf

moveit_commander.roscpp_initialize(sys.argv)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()

group = moveit_commander.MoveGroupCommander('right_arm')

rospy.init_node('Quickstart')
right = baxter_interface.Limb('right')
left = baxter_interface.Limb('left')

right_gripper = Gripper('right')
left_gripper = Gripper('left')

#start the listener
"""
listener = tf.TransformListener()


rospy.sleep(2) # waits for data to be published to topic. tf will grab last-published position

for i in range(0,5):
	try:
		(trans,rot) = listener.lookupTransform('/right_gripper', '/base', rospy.Time(0))
		# Look up the position of the right gripper w.r.t. base
		# ((x, y, z), (x, y, z, w))
		break
	except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
	    continue
	sleep(2)

pos1 = ((0.7306702209246183, 0.28223929794476754, 0.2367945290045651), (0.0217668190740447, 0.9996525747530348, -0.01104966087353584, 0.009941849506288689))

pos2 = ((0.9026802089218793, 0.20021166217435235, 0.1974968069962135), (0.38410200772926917, 0.9231271050045804, -0.0076375860357680864, -0.015609706715791065))

"""
position1 = [0.6, -.3, 0, 0.0217668190740447, 0.9996525747530348, -0.01104966087353584, 0.009941849506288689]
position2 = [-.3, -.3, 0.1974968069962135, 0.38410200772926917, 0.9231271050045804, -0.0076375860357680864, -0.015609706715791065]

#Change velocity of the movement
group.set_max_velocity_scaling_factor(0.6)

raw_input("========== Press enter to order robot to move 1.")
group.set_joint_value_target(position1)
group.plan()
group.go()

group.set_max_velocity_scaling_factor(1.0)

raw_input("========== Press enter to order robot to move 2.")
group.set_joint_value_target(position2)
group.plan()
group.go()




