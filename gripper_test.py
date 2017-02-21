#import sys
#import copy
import rospy
#import moveit_commander
#import moveit_msgs.msg 
#import geometry_msgs.msg
import baxter_interface
from baxter_interface import Gripper
#from baxter_interface import CHECK_VERSION

rospy.init_node('Grip_Test')
right = baxter_interface.Limb('right')

right_gripper = Gripper('right')
left_gripper = Gripper('left')

#left, right, from view facing baxter
angles = {}
angles['intermediate'] = {'right_s0': 1.0009224640952326, 'right_s1': -0.7980535048973865, 'right_w0': 0.14764565083397108, 'right_w1': 1.5792332211280335, 'right_w2': 1.3349467806572812, 'right_e0': -0.24812139244046566, 'right_e1': 0.8889418665795973}
angles['left_above'] = {'right_s0': 0.7002622296696914, 'right_s1': -0.9951700361406621, 'right_w0': -0.022626216621309852, 'right_w1': 0.9974710073224903, 'right_w2': 0.5035291936233871, 'right_e0': -0.08206797215186963, 'right_e1': 1.4714710707790832}
angles['left_in'] = {'right_s0': 0.6293156182299909, 'right_s1': -0.7784952498518475, 'right_w0': 0.10891263593986437, 'right_w1': 0.9161700255645634, 'right_w2': 0.6653641667452982, 'right_e0': -0.041033986075934815, 'right_e1': 1.4150972768242942}
angles['right_above'] = {'right_s0': 1.2221991927477034, 'right_s1': -0.6580777580028425, 'right_w0': 0.1062281695610649, 'right_w1': 1.358339987672534, 'right_w2': 1.2340875438538152, 'right_e0': -0.18676216092504913, 'right_e1': 0.9180875015494201}
angles['right_in'] = {'right_s0': 1.2329370582629013, 'right_s1': -0.6350680461845613, 'right_w0': 0.09203884727312482, 'right_w1': 0.9456991557313575, 'right_w2': 1.2459758949599273, 'right_e0': -0.14534467965214296, 'right_e1': 1.1577719996565161}


def move_to(pos):
#	right.move_to_joint_positions(angles['intermediate'])
	right.move_to_joint_positions(angles[pos+'_above'])

def pick_up(pos):
	right.move_to_joint_positions(angles[pos+'_in'])
	right_gripper.close()
	rospy.sleep(1)
	right.move_to_joint_positions(angles[pos+'_above'])

def drop(pos):
	right.move_to_joint_positions(angles[pos+'_in'])
	right_gripper.open()
	rospy.sleep(1)
	right.move_to_joint_positions(angles[pos+'_above'])

def begin_to_end(pos_A, pos_B):
	move_to(pos_A)
	pick_up(pos_A)
	move_to(pos_B)
	drop(pos_B)

if __name__ == "__main__":
	right_gripper.open()
	right.move_to_joint_positions(angles['intermediate'])
	for i in range(2):
		begin_to_end('left', 'right')
		begin_to_end('right', 'left')
	right.move_to_joint_positions(angles['intermediate'])