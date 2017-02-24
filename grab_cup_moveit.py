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
group = moveit_commander.MoveGroupCommander('right_arm')

# Create DisplayTrajectory publisher to publish trajectories for RVIZ
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
	moveit_msgs.msg.DisplayTrajectory)



positions = {
	'neutral': ((0.3198243428112764, -0.7329243799821087, 0.23516284576053526), (0.7068531083265872, 0.7062452313309197, -0.03904328216040395, 0.007209617848457904)),
	'up_left': ((0.2142508091922578, -0.9288363476671154, 0.12694096746125721), (0.8457825402532808, 0.5324487125861679, -0.02886542421603567, -0.01780590780803439)),
	'grab_left': ((0.22580413777113795, -0.9385228087003921, -0.02132673374264328), (0.8373016904925557, 0.5439085734409956, -0.044799568244231744, -0.03289895926651958)),
	'up_right': ((0.07693566524260859, -0.8417540328542379, 0.03573798270901427), (0.7182457952950193, 0.693510265556497, 0.021078169747311422, -0.05217470525921396)),
	'grab_right': ((-0.006174042880000563, -0.8516386169774242, -0.08565906653496354), (0.7496541227702167, 0.6594589511332506, 0.019346268352611523, -0.05251961428531979))
}

def makeTargetPose(coords):
	"""Takes a tuple of translational & rotational coordinates. Creates and returns 
	a new Pose object with those coordinates."""
	new_pose = geometry_msgs.msg.Pose()
	new_pose.position.x = coords[0][0]
	new_pose.position.y = coords[0][1]
	new_pose.position.z = coords[0][2]
	new_pose.orientation.x = coords[1][0]
	new_pose.orientation.y = coords[1][1]
	new_pose.orientation.z = coords[1][2]
	new_pose.orientation.w = coords[1][3]
	return new_pose

waypoints = [makeTargetPose(positions['neutral']),
			makeTargetPose(positions['up_left']),
			makeTargetPose(positions['grab_left'])]

###### Testing normal Cartesian movement ######
for w in waypoints:
	group.clear_pose_targets()
	group.set_pose_target(w)
	plan = group.plan()
	print("==== Destination Translational Coords ====")
	print(w.position)
	raw_input("========== Press enter to order robot to move.")
	group.go(wait=True)


###### Testing waypoints ######

print(waypoints)

(plan, fraction) = group.compute_cartesian_path(waypoints, 0.01, 0.0)

raw_input("========== Press enter to order robot to move.")
group.go(wait=True)

