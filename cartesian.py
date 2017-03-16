import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()

group = moveit_commander.MoveGroupCommander('right_arm')

# display_trajectory_publisher = rospy.Publisher(
#                                     '/move_group/display_planned_path',
#                                     moveit_msgs.msg.DisplayTrajectory)

# rospy.sleep(5)
print "============ Reference frame: %s" % group.get_planning_frame()
print "============ Reference frame: %s" % group.get_end_effector_link()
print "============ Robot Groups:"
print robot.get_group_names()
print "============ Printing robot state"
print robot.get_current_state()
print "============"
print "============ Generating plan 1"

pose_target = geometry_msgs.msg.Pose()
# pose_target.orientation.w = 1.0
pose_target.position.x = 0.7
pose_target.position.y = 0.05
pose_target.position.z = 1.1
while True:
	raw_input("Press Enter")
	
	group.set_pose_target(pose_target)
	print(pose_target)
	plan = group.plan()
	group.go(wait=True)

	# pose_target.orientation.w -= 0.1
	pose_target.position.x -= 0.1
	pose_target.position.y -= 0.1
	pose_target.position.z -= 0.1


# waypoints = []

# # start with the current pose
# waypoints.append(group.get_current_pose().pose)

# # first orient gripper and move forward (+x)
# wpose = geometry_msgs.msg.Pose()
# wpose.orientation.w = 1.0
# wpose.position.x = waypoints[0].position.x + 0.1
# wpose.position.y = waypoints[0].position.y
# wpose.position.z = waypoints[0].position.z
# waypoints.append(copy.deepcopy(wpose))

# # second move down
# wpose.position.z -= 0.10
# waypoints.append(copy.deepcopy(wpose))

# # third move to the side
# wpose.position.y += 0.05

# waypoints.append(copy.deepcopy(wpose))
# (plan3, fraction) = group.compute_cartesian_path(
#                              waypoints,   # waypoints to follow
#                              0.01,        # eef_step
#                              0.0)         # jump_threshold

# print "============ Waiting while RVIZ displays plan3..."
# rospy.sleep(5)

