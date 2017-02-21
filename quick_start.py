import rospy
import baxter_interface
from baxter_interface import Gripper

rospy.init_node('Quickstart')
right = baxter_interface.Limb('right')
left = baxter_interface.Limb('left')

right_gripper = Gripper('right')
left_gripper = Gripper('left')