
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg 
import geometry_msgs.msg
import baxter_interface
from sensor_msgs.msg import PointCloud
from baxter_interface import Gripper
import tf


def move_to_point(point):
	pose_target = geometry_msgs.msg.Pose()
	pose_target.orientation.w = 1.0
	pose_target.position.x = point.x
	pose_target.position.y = point.y
	pose_target.position.z = point.z
	print(pose_target)
	group.set_pose_target(pose_target)
	plan = group.plan()
	group.go(wait=True)
	rospy.signal_shutdown('end program')

def callback(data):
	t = listener.transformPointCloud('/base', data)
	# print(t.points[0])
	move_to_point(t.points[0])
	subscriber.unregister()

if __name__ == '__main__':
	rospy.init_node('Follow')

	group = moveit_commander.MoveGroupCommander('right_arm')

	listener = tf.TransformListener()
	subscriber = rospy.Subscriber('mocap_point_cloud', PointCloud, callback)	
	rospy.spin()


"""
# make a waypoint
waypoint = makeTargetPose([translation,rotation])

# reset the group coordinates
group.clear_pose_targets()
# set group coordinate 
group.set_pose_target(waypoint)
# plan the path
plan = group.plan()
print("==== Destination Translational Coords ====")
print(waypoint.position)
# move the robot
raw_input("========== Press enter to order robot to move.")
group.go(wait=True)
"""








# helper function
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