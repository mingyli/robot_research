# Working from the moveit tutorials online
# 
# 

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg 
import geometry_msgs.msg
import baxter_interface
import time

# Initializes moveit_commander & rospy
print("========== Starting tutorial setup")
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

# Instantiates a RobotCommander object and PlanningSceneInterface object
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()

# Instantiates a MoveGroupCommander object, interfaces w/ right arm joints
group = moveit_commander.MoveGroupCommander('right_arm')

# Create DisplayTrajectory publisher to publish trajectories for RVIZ
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
	moveit_msgs.msg.DisplayTrajectory)

# # Wait for RVIZ to initialize 
# print("========== Waiting for RVIZ...")
# rospy.sleep(10)
# print("========== Starting tutorial")

# Refer to moveit documentation for more information about poses


#rospy.init_node('Hello_Baxter')

# create an instance of baxter_interface's Limb class
limb = baxter_interface.Limb('right')

# get the right limb's current joint angles

angles = {'right_s0': 1.3717623195665312, 'right_s1': -0.5108156023658428, 'right_w0': 0.7988204952913293, 'right_w1': 1.0488593637166517, 'right_w2': 1.2620826932327243, 'right_e0': -0.9449321653374149, 'right_e1': 1.4415584454153176}
limb.move_to_joint_positions(angles)

print("========== Printing current group pose")
while(True):
	curr_pose = group.get_current_pose().pose
	print(curr_pose)
	time.sleep(0.1)