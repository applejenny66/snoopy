#!/usr/bin/env python

"""
import moveit_commander
from geometry_msgs.msg import Pose, Quaternion
from tf.transformations import quaternion_from_euler
"""
from genwords import new_img, word_table, all_stroke

def set_home(x, y, z):
    home_point = (x, y, z)
    return (home_point)


def go_point():
    pass




group= moveit_commander.MoveGroupCommander("arm")

ps = Pose()
ps.position.x = 0.9 
ps.position.y = 0.1
ps.position.z = 0.1 
ps.orientation = Quaternion(*quaternion_from_euler(1.57, 0.000, 0.00, 'syxz'))

group.set_pose_target(ps)
group.go()

def main():
    home_point = set_home(0.9, 0.1, 0.1) # setting home first
    total_stroke = all_stroke()
    print ("total stroke: ", total_stroke)




if __name__ == "__main__":
    total_stroke = all_stroke()
    print ("total stroke: ", total_stroke)
    pass

