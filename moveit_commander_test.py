# Working from the moveit tutorials online
# 
# 

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg 
import geometry_msgs.msg

# Initializes moveit_commander & rospy
print("========== Starting tutorial setup")
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

# Instantiates a RobotCommander object and PlanningSceneInterface object
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()

# Instantiates a MoveGroupCommander object, interfaces w/ right arm joints
group = moveit_commander.MoveGroupCommander('left_arm')

# Create DisplayTrajectory publisher to publish trajectories for RVIZ
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
	moveit_msgs.msg.DisplayTrajectory)

# # Wait for RVIZ to initialize 
# print("========== Waiting for RVIZ...")
# rospy.sleep(10)
# print("========== Starting tutorial")

# Refer to moveit documentation for more information about poses
print("========== Printing current group pose")
curr_pose = group.get_current_pose().pose
print(curr_pose)

# Generating a plan to move to a pose goal (same as dragging around the nodes in Rviz)
# THIS DOESN'T SEEM TO WORK FOR SOME ODD REASON
# This is position 1
print("=========== Moving arm to certain cartesian coords")
pose_target = geometry_msgs.msg.Pose() # hopefully copies the current pose
pose_target.orientation.w = 1.0
pose_target.position.x = 0.7
pose_target.position.y = 0.1
pose_target.position.z = 1.0

group.set_pose_target(pose_target) # Set the pose target of the group

plan1 = group.plan() # Tell the planner to plan out the motions required
print("========== Pausing for RVIZ to display")
rospy.sleep(5)

raw_input("========== Press enter to order robot to move.")
group.go(wait=True) # Now make the robot move!



print("========== Clearing pose targets, now setting joint targets ")
group.clear_pose_targets()

print("========== Getting joint values")
group_variable_values = group.get_current_joint_values()
print(group_variable_values)

# Generating a plan to move to a joint-space goal (set all joints to certain position)
group_variable_values = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] # reset
print("========== Moving left arm to straight position")
group.set_joint_value_target(group_variable_values)
plan2 = group.plan()
print("========== Pausing for RVIZ to display")
rospy.sleep(5)

raw_input("========== Press enter to order robot to move.")
group.go(wait=True)


print("========== Now doing waypoints")
waypoints = []

# start with current pose
waypoints.append(group.get_current_pose().pose)

# move back (-x)
wpose = geometry_msgs.msg.Pose()
wpose.orientation.w = 1.0
wpose.position.x = waypoints[0].position.x -0.5
wpose.position.y = waypoints[0].position.y
wpose.position.z = waypoints[0].position.z
waypoints.append(copy.deepcopy(wpose))

# move up
wpose.position.z += 5
waypoints.append(copy.deepcopy(wpose))

(plan3, fraction) = group.compute_cartesian_path(waypoints, 0.01, 0.0) # compute path with 1cm resolution, no jump thresh
print("========== Pausing for RVIZ to display")
rospy.sleep(5)

raw_input("========== Press enter to order robot to move.")
group.go(wait=True)


raw_input("========== Press enter to quit")
moveit_commander.roscpp_shutdown()