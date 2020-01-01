#!/usr/bin/env python


import moveit_commander
from geometry_msgs.msg import Pose, Quaternion
from tf.transformations import quaternion_from_euler


group= moveit_commander.MoveGroupCommander("arm")

ps = Pose()
ps.position.x = 0.9 
ps.position.y = 0.1
ps.position.z = 0.1 
ps.orientation = Quaternion(*quaternion_from_euler(1.57, 0.000, 0.00, 'syxz'))

group.set_pose_target(ps)
group.go()

