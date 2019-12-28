#!/usr/bin/env python

"""
import moveit_commander
from geometry_msgs.msg import Pose, Quaternion
from tf.transformations import quaternion_from_euler
"""
from genwords import new_img, word_table, all_stroke


class painting():
    def __init__(self):
        self.total_stroke = []
        self.group= moveit_commander.MoveGroupCommander("arm")

        self.ps = Pose()
        self.ps.position.x = 0.9 
        self.ps.position.y = 0.1
        self.ps.position.z = 0.1 
        self.ps.orientation = Quaternion(*quaternion_from_euler(1.57, 0.000, 0.00, 'syxz'))
        self.z_up = 0.3
        self.z_down = 0.2

    def mapping(self, map_table):
        self.map_table = map_table

    def stroke(self, total_stroke):
        self.total_stroke = total_stroke

    def set_home(self, x, y, z):
        home_point = (x, y, z)
        self.home = home_point
        #return (home_point)

    def go_point(self, x, y, z):
        self.ps.position.x = x
        self.ps.position.y = y
        self.ps.position.z = z
        self.group.set_pose_target(self.ps)
        self.group.go()
        print ("going")

    def go_up(self):
        self.ps.position.z = self.z_up
        self.group.set_pose_target(self.ps)
        self.group.go()
        print ("up")

    def go_down(self):
        self.ps.position.z = self.z_down
        self.group.set_pose_target(self.ps)
        self.group.go()
        print ("down")

    def start_painting(self):
        len_words = len(self.total_stroke)
        for i in range(0, len_words):
            total_point = self.total_stroke[i]
            len_total_point = len(total_point)
            for j in range(0, len_total_point):
                tmp_x = total_point[j][0]
                tmp_y = total_point[j][1]
                if (j == 0):
                    self.go_up()
                    self.go_point(tmp_x, tmp_y, self.z_up)
                    self.go_down()
                else:
                    if ((tmp_x == -1) or (tmp_y == -1)):
                        self.go_up()
                        if (j+1 > len_total_point-1):
                            pass
                        else:
                            next_x = total_point[j+1][0]
                            next_y = total_point[j+1][1]
                            self.go_point(next_x, next_y, self.z_up)
                    else:
                        self.go_point(tmp_x, tmp_y, self.z_down)
            self.go_up()
        



def main():
    new_painting = painting()
    total_stroke = all_stroke()
    new_painting.stroke(total_stroke)
    new_painting.set_home(0.9, 0.1, 0.1)
    #new_painting.mapping(map_table)
    new_painting.start_painting()
    #home_point = set_home(0.9, 0.1, 0.1) # setting home first
    
    print ("total stroke: ", total_stroke)




if __name__ == "__main__":
    total_stroke = all_stroke()
    print ("total stroke: ", total_stroke)
    pass

