# Working from the moveit tutorials online
# 
# 

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg 
import geometry_msgs.msg
from baxter_interface import Gripper

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

right_gripper = Gripper('right')
left_gripper = Gripper('left')


"""
{'right_s0': 1.3717623195665312, 'right_s1': -0.5108156023658428, 'right_w0': 0.7988204952913293, 'right_w1': 1.0488593637166517, 'right_w2': 1.2620826932327243, 'right_e0': -0.9449321653374149, 'right_e1': 1.4415584454153176}

"""
print("========== Printing current group pose")
curr_pose = group.get_current_pose().pose
print(curr_pose)

# Generating a plan to move to a pose goal (same as dragging around the nodes in Rviz)
# This is position 1
print("=========== Moving arm to certain cartesian coords")
pose_target = geometry_msgs.msg.Pose() # hopefully copies the current pose
pose_target.orientation.w = 1.0
pose_target.position.x = 0.6
pose_target.position.y = -0.34
pose_target.position.z = 0.10

group.set_pose_target(pose_target) # Set the pose target of the group

plan1 = group.plan() # Tell the planner to plan out the motions required
print("========== Pausing for RVIZ to display")
rospy.sleep(5)

raw_input("========== Press enter to order robot to move.")
group.go(wait=True) # Now make the robot move!

# Generating a plan to move to a pose goal (same as dragging around the nodes in Rviz)
# This is position 1
print("=========== Moving arm to certain cartesian coords")
pose_target = geometry_msgs.msg.Pose() # hopefully copies the current pose
pose_target.orientation.w = 1.0
pose_target.position.x = 0.6
pose_target.position.y = -0.34
pose_target.position.z = 0.05

group.set_pose_target(pose_target) # Set the pose target of the group

plan1 = group.plan() # Tell the planner to plan out the motions required
print("========== Pausing for RVIZ to display")
rospy.sleep(5)

raw_input("========== Press enter to order robot to move.")
group.go(wait=True) # Now make the robot move!

