# offset_test.py

#!/usr/bin/env python


import moveit_commander
from geometry_msgs.msg import Pose, Quaternion
from tf.transformations import quaternion_from_euler

from genwords import new_img, word_table, all_stroke
from offset import offset

class painting():
    def __init__(self, offset_table):
        self.original_stroke = []
        self.total_stroke = []

        self.group= moveit_commander.MoveGroupCommander("arm")
        self.offset_table = offset_table
        self.ps = Pose()
        self.ps.position.x = 0.7
        self.ps.position.y = 0.2
        self.ps.position.z = 0.4
        self.ps.orientation = Quaternion(*quaternion_from_euler(1.57, 0.000, 0.00, 'syxz'))
        self.z_up = 0.4
        self.z_down = 0.25

    def pigment(self):
        self.go_up()
        self.ps.position.x = 0.7
        self.ps.position.y = 0.3
        self.ps.position.z = 0.25
        self.group.set_pose_target(self.ps)
        self.group.go()
        print ("going to pigment")
        self.ps.position.x = 0.69
        self.ps.position.y = 0.29
        self.group.set_pose_target(self.ps)
        self.group.go()
        self.ps.position.x = 0.7
        self.ps.position.y = 0.3
        self.ps.position.z = 0.25
        self.group.set_pose_target(self.ps)
        self.group.go()
        self.ps.position.z = 0.4
        self.group.set_pose_target(self.ps)
        self.group.go()

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
        x_list = [0.7,  0.72,  0.74, 0.76,  0.78, 0.8,   0.82, 0.84, 0.86, 0.88, 0.9]
        y_list = [-0.3, -0.25, -0.2, -0.15, -0.1, -0.05, 0,    0.05, 0.1,  0.15, 0.2]
        len_words = len(self.total_stroke)
        for i in range(0, len_words):
            self.pigment()
            print ("i: ", i)
            total_point = self.total_stroke[i]
            origin_point = self.original_stroke[i]
            len_total_point = len(total_point)
            for j in range(0, len_total_point):
                tmp_x = total_point[j][0]
                tmp_y = total_point[j][1]
                ori_x = origin_point[j][0]
                ori_y = origin_point[j][1]
                #total_len = len(total_stroke)
                for p in range(0, len_words): #0
                    for q in range(0, len(self.total_stroke[p])):
                        tmp_stroke = self.total_stroke[p][q]
                        tmp_stroke_x = tmp_stroke[0]
                        tmp_stroke_y = tmp_stroke[1]
                        min_x_dev = 1
                        min_x_index = 0
                        min_y_dev = 1
                        min_y_index = 0
                        for m in range(0, 11):
                            if (abs(tmp_stroke_x - x_list[m]) < min_x_dev):
                                min_x_dev = abs(tmp_stroke_x - x_list[m])
                                min_x_index = m
                            if (abs(tmp_stroke_y - y_list[m]) < min_y_dev):
                                min_y_dev = abs(tmp_stroke_y - y_list[m])
                                min_y_index = m
                            #z_index = min_x_index * 11 + min_y_index + 1
                        self.z_down = 0.25 + round(self.offset_table[min_x_index, min_y_index][0], 3)    
                print ("x, y, z: ", tmp_x, tmp_y, self.z_down)

                if (j == 0):
                    self.go_up()
                    self.go_point(tmp_x, tmp_y, self.z_up)
                    self.go_down()
                    self.ps.position.x = tmp_x
                    self.ps.position.y = tmp_y
                else:
                    if ((ori_x == -1) and (ori_y == -1)):
                        #self.go_point(self.ps.position.x, self.ps.position.y, self.z_up)
                        self.go_up()
                        if (j+1 > len_total_point-1):
                            pass
                        else:
                            next_x = total_point[j+1][0]
                            next_y = total_point[j+1][1]
                            self.go_point(next_x, next_y, self.z_up)
                    else:
                        self.go_point(tmp_x, tmp_y, self.z_down)
                        self.ps.position.x = tmp_x
                        self.ps.position.y = tmp_y
            self.go_up()

def test_go_point(x, y, z):
    group= moveit_commander.MoveGroupCommander("arm")
    ps = Pose()
    ps.position.x = x 
    ps.position.y = y
    ps.position.z = z
    ps.orientation = Quaternion(*quaternion_from_euler(1.57, 0.000, 0.00, 'syxz'))
    group.set_pose_target(ps)
    group.go()
    print ("going: ", x, y, z)


def offset_test(offset_table):
    # (0.7, 0.2)-----------(0.9, 0.2)
    #          |           |
    #          |           |
    #          |           |
    # (0.7, -0.3)----------(0.9, -0.3)
    #print ("table shape: ", offset_table.shape)
    #print ("z tmp: ", round(offset_table[10,10][0], 3))
    origin_x = 0.7
    origin_y = 0.2
    origin_z = 0.25
    count = 0
    for i in range(0, 11):
        for j in range(0, 11):
            y = round(origin_y - (i * 0.05), 3)
            x = round(origin_x + (j * 0.02), 3)
            offset_z = round(offset_table[i, j][0], 3)
            z = round((origin_z - offset_z), 3)
            #print (x, y, z)
            count += 1
            test_go_point(x, y, z)
    #print ("total count: ", count)




def main():
    offset_table = offset()
    test_go_point(0.7, 0.2, 0.4)
    #offset_test(offset_table)

    new_painting = painting(offset_table)
    new_painting.set_home(0.7, 0.2, 0.4)

    total_stroke = all_stroke()
    new_painting.original_stroke = total_stroke
    print ("ori total stroke: ", new_painting.original_stroke)
    new_stroke = all_stroke()
    #print ("total stroke: ", total_stroke)


    
    #print ("len: ", len(total_stroke))
    
    total_len = len(new_stroke)
    for i in range(0, total_len):
        for j in range(0, len(total_stroke[i])):
            tmp_point = new_stroke[i][j]
            tmp_point[0] = round((float(tmp_point[0]) / 100) + 0.7, 3)
            tmp_point[1] = round(((float(tmp_point[1]) / 100) / 1.32 - 0.3), 3)
            new_stroke[i][j] = (tmp_point[0], tmp_point[1])
    #print ("new stroke: ", new_stroke)
        
    #for i in range(0, len(t))
    new_painting.stroke(new_stroke)
    #print ("ori total stroke: ", new_painting.original_stroke)

    #print ("stroke: ", new_painting.total_stroke)
    
    #new_painting.mapping(map_table)
    

    new_painting.start_painting()


    #home_point = set_home(0.9, 0.1, 0.1) # setting home first
    
    #print ("total stroke: ", total_stroke)




if __name__ == "__main__":
    test_go_point(0.7, 0.3, 0.4)
    main()
    #test_go_point(0.7, 0.2, 0.4)
    #test_go_point(0.7, 0.2, 0.25)
    #total_stroke = all_stroke()
    #print ("total stroke: ", total_stroke)
    
    pass


