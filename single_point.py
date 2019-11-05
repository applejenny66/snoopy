#!/usr/bin/env python


import moveit_commander
from geometry_msgs.msg import Pose, Quaternion
from tf.transformations import quaternion_from_euler


group= moveit_commander.MoveGroupCommander("arm")

ps = Pose()
ps.position.x = 0.9 #forward
ps.position.y = 0.1 #left
ps.position.z = 0.2 #upward
ps.orientation = Quaternion(*quaternion_from_euler(1.57, 0.00, 0.00, 'syxz')) #angular

group.set_pose_target(ps)
group.go()

