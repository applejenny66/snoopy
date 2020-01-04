import cv2 
import numpy as np
import os
import csv
import math

#clouds and 10
# thunderstorms 13
sqrt = math.sqrt
pi = math.pi
cos = math.cos
sin = math.sin

def new_img(shape):
    #shape = (5,5,1)
    img = np.zeros((shape))
    for x in range(0, shape[0]):
        for y in range(0, shape[1]):
            img[x, y, 0] = img[x, y, 1] = img[x, y, 2] = 255
    return (img)

def stroke_table():
    stroke_dict = {}
    #c
    stroke_c_right = []
    for i in range(-20, 5):
        tmp_list = []
        tmp_angle = i * pi / 16
        tmp_x = round(3 + cos(tmp_angle), 3)
        tmp_y = round(1 + sin(tmp_angle), 3)
        tmp_list.append(tmp_x)
        tmp_list.append(tmp_y)
        stroke_c_right.append(tmp_list)
        #print (i, ": ", tmp_list)
    #print ("test: ", cos(pi), sin(pi))
    #print ("stroke c: ", stroke_c_right)
    stroke_dict['c_right'] = stroke_c_right

    # c <-
    stroke_c_left = []
    for i in range(20, -5, -1):
        tmp_list = []
        tmp_angle = i * pi / 16
        tmp_x = round(3 + cos(tmp_angle), 3)
        tmp_y = round(1 + sin(tmp_angle), 3)
        tmp_list.append(tmp_x)
        tmp_list.append(tmp_y)
        stroke_c_left.append(tmp_list)
        #print (i, ": ", tmp_list)
    stroke_dict['c_left'] = stroke_c_left

    # r
    stroke_r = []
    for i in range(24, 11, -1):
        tmp_list = []
        tmp_angle = i * pi / 16
        tmp_x = round(3 + cos(tmp_angle), 3)
        tmp_y = round(1 + sin(tmp_angle), 3)
        tmp_list.append(tmp_x)
        tmp_list.append(tmp_y)
        stroke_r.append(tmp_list)
    stroke_dict['r'] = stroke_r

    # n
    stroke_n = stroke_r
    stroke_n.append([4, 2])
    stroke_dict['n'] = stroke_n
    
    # half-circle (open below)
    stroke_half_cirle_below = []
    for i in range(24, 7, -1):
        tmp_list = []
        tmp_angle = i * pi / 16
        tmp_x = round(3 + cos(tmp_angle), 3)
        tmp_y = round(1 + sin(tmp_angle), 3)
        tmp_list.append(tmp_x)
        tmp_list.append(tmp_y)
        stroke_half_cirle_below.append(tmp_list)
        stroke_half_cirle_below.append([4, 2])
    stroke_dict['half_circle_below'] = stroke_half_cirle_below

    # o
    stroke_o = []
    for i in range(24, -9, -1):
        tmp_list = []
        tmp_angle = i * pi / 16
        tmp_x = round(3 + cos(tmp_angle), 3)
        tmp_y = round(1 + sin(tmp_angle), 3)
        tmp_list.append(tmp_x)
        tmp_list.append(tmp_y)
        stroke_o.append(tmp_list)
    stroke_dict['o'] = stroke_o

    # .
    stroke_dot = [[1,1]]
    stroke_dict['dot'] = stroke_dot
    # -
    stroke_line_top = [[2, 0], [2, 2]]
    stroke_line_middle = [[3, 0], [3, 2]]
    stroke_line_below = [[4, 0], [4, 2]]
    
    stroke_dict['line_top'] = stroke_line_top
    stroke_dict['line_middle'] = stroke_line_middle
    stroke_dict['line_below'] = stroke_line_below

    # l
    stroke_l_a_left = [[0, 0], [4, 0]]
    stroke_l_a_middle = [[0, 1], [4, 1]]
    stroke_l_a_right = [[0, 2], [4, 2]]
    stroke_l_b_left = [[2, 0], [6, 0]]
    stroke_l_b_right = [[2, 2], [6, 2]]
    stroke_l_short_left = [[2, 0], [4, 0]]
    stroke_l_short_middle = [[2, 1], [4, 1]]
    stroke_l_short_right = [[2, 2], [4, 2]]
    
    stroke_dict['l_a_left'] = stroke_l_a_left
    stroke_dict['l_a_middle'] = stroke_l_a_middle
    stroke_dict['l_a_right'] = stroke_l_a_right
    stroke_dict['l_b_left'] = stroke_l_b_left
    stroke_dict['l_b_right'] = stroke_l_b_right
    stroke_dict['l_short_left'] = stroke_l_short_left
    stroke_dict['l_short_middle'] = stroke_l_short_middle
    stroke_dict['l_short_right'] = stroke_l_short_right

    # k
    stroke_k = [[2,2], [3, 0], [4, 2]]
    stroke_dict['k'] = stroke_k

    
    # j below
    stroke_j_like = [[2, 2], [4, 2]]
    for i in range(16, -1, -1):
        tmp_list = []
        tmp_dev = float(i) / 8.0
        tmp_y = round(tmp_dev, 3)
        tmp = (tmp_dev - 1) * (tmp_dev - 1) * (-2) + 6
        tmp_x = round(tmp, 3)
        tmp_list.append(tmp_x)
        tmp_list.append(tmp_y)
        stroke_j_like.append(tmp_list)
    stroke_dict['j_like'] = stroke_j_like
    stroke_j = stroke_j_like
    stroke_j.append([-1, -1])
    stroke_j.append([1, 2])
    stroke_dict['j'] = stroke_j
    
    # f
    stroke_f = []
    for i in range(16, 7, -1):
        tmp_list = []
        tmp_dev = float(i) / 8.0
        tmp_y = round(tmp_dev, 3)
        tmp = (tmp_dev - 1.5) * (tmp_dev - 1.5) * 4
        tmp_x = round(tmp, 3)
        tmp_list.append(tmp_x)
        tmp_list.append(tmp_y)
        stroke_f.append(tmp_list)
    stroke_f.append([4, 1])
    stroke_dict['f'] = stroke_f

    
    # u
    stroke_u = [[2, 0], [3, 0]]
    for i in range(-4, 5):
        tmp_list = []
        tmp_angle = i * pi / 16
        tmp_x = round(3 + cos(tmp_angle), 3)
        tmp_y = round(1 + sin(tmp_angle), 3)
        tmp_list.append(tmp_x)
        tmp_list.append(tmp_y)
        stroke_u.append(tmp_list)
    stroke_u.append([2, 2])
    stroke_u.append([4, 2])
    stroke_dict['u'] = stroke_u
    
    # t
    stroke_t = [[2, 0], [2, 2], [-1, -1], [1, 1], [3, 1]]
    for i in range(16, 33):
        tmp_list = []
        tmp_dev = float(i) / 16.0
        tmp_y = round(tmp_dev, 3)
        tmp = (tmp_dev - 1.5) * (tmp_dev - 1.5) * (-4) + 4
        tmp_x = round(tmp, 3)
        tmp_list.append(tmp_x)
        tmp_list.append(tmp_y)
        stroke_t.append(tmp_list)
    stroke_dict['t'] = stroke_t

    # part of a
    stroke_part_a = [[3 + cos(3 * pi / 4), 1 + sin(3 * pi / 4)], [4, 2]]
    stroke_dict['part_a'] = stroke_part_a
    # v
    stroke_v = [[2, 0], [4, 1], [2, 2]]
    stroke_dict['v'] = stroke_v
    # x
    stroke_x = [[2, 0], [4, 2], [-1, -1], [2, 2], [4, 0]]
    stroke_dict['x'] = stroke_x
    # y
    stroke_y = [[2, 0], [4, 1], [-1, -1], [2, 2], [6, 0]]
    stroke_dict['y'] = stroke_y
    # z middle of z
    stroke_z = [[2, 2], [4, 0]]
    stroke_dict['z'] = stroke_z
    # s
    stroke_s = []
    for i in range(12, 7, -1):
        tmp_list = []
        tmp_dev = float(i) / 8.0
        tmp_y = round(tmp_dev, 3)
        tmp = (tmp_dev - 2.5) * (tmp_dev -2.5) * (-2) + 1.5
        tmp_x = round(tmp, 3)
        tmp_list.append(tmp_x)
        tmp_list.append(tmp_y)
        stroke_s.append(tmp_list)
    for j in range(16, 25):
        tmp_list = []
        tmp_dev = float(j) / 8.0
        tmp_x = round(tmp_dev, 3)
        tmp = (tmp_dev - 2.5) * (tmp_dev - 2.5) * 2 + 0.5
        tmp_y = round(tmp, 3)
        tmp_list.append(tmp_x)
        tmp_list.append(tmp_y)
        stroke_s.append(tmp_list)
    for k in range(24, 33):
        tmp_list = []
        tmp_dev = float(k) / 8.0
        tmp_x = round(tmp_dev, 3)
        tmp = (tmp_dev - 3.5) * (tmp_dev - 3.5) * (-2) + 1.5
        tmp_y = round(tmp, 3)
        tmp_list.append(tmp_x)
        tmp_list.append(tmp_y)
        stroke_s.append(tmp_list)
    for m in range(32, 27, -1):
        tmp_list = []
        tmp_dev = float(m) / 8.0
        tmp_x = round(tmp_dev, 3)
        tmp = (tmp_dev - 3.5) * (tmp_dev - 3.5) * 2 + 0.5
        tmp_y = round(tmp, 3)
        tmp_list.append(tmp_x)
        tmp_list.append(tmp_y)
        stroke_s.append(tmp_list)
    stroke_dict['s'] = stroke_s

    # w
    stroke_w = [[2, 0], [4, 0.5], [2, 1], [4, 1.5], [2,2]]
    stroke_dict['w'] = stroke_w

    # m
    stroke_m = [[2, 0], [4, 0]]
    for i in range(-4, 5):
        tmp_list = []
        tmp_angle = (i * pi / 8)
        tmp_x = round(0.5 * cos(tmp_angle) + 2.5, 3)
        tmp_y = round(0.5 * sin(tmp_angle) + 0.5, 3)
        tmp_list.append(tmp_x)
        tmp_list.append(tmp_y)
        stroke_m.append(tmp_list)
    stroke_m.append([4, 1])
    for j in range(-4, 5):
        tmp_list = []
        tmp_angle = (j * pi / 8)
        tmp_x = round(0.5 * cos(tmp_angle) + 2.5, 3)
        tmp_y = round(0.5 * sin(tmp_angle) + 1.5, 3)
        tmp_list.append(tmp_x)
        tmp_list.append(tmp_y)
        stroke_m.append(tmp_list)
    stroke_m.append([4, 2])
    stroke_dict['m'] = stroke_m

    return (stroke_dict)

def word_stroke(stroke_dict):
    print ("key: ", stroke_dict.keys())
    # ('key: ', ['l_b_left', 'c_left', 'l_short_middle', 'part_a', 'line_below', 
    # 'line_middle', 'half_circle_below', 'l_a_left', 'v', 'x', 'l_short_right', 
    # 'line_top', 'f', 'l_b_right', 'k', 'j', 'o', 's', 'r', 'u', 't', 'j_like',
    # 'l_a_right', 'c_right', 'y', 'l_short_left', 'l_a_middle', 'z', 'dot'])
    
    word_a = stroke_dict['c_right'] + stroke_dict['part_a']
    word_b = stroke_dict['l_a_left'] + stroke_dict['c_left']
    word_c = stroke_dict['c_right']
    word_d = stroke_dict['c_right'] + stroke_dict['l_a_right']
    word_e = stroke_dict['line_middle'] + stroke_dict['c_right']
    word_f = stroke_dict['line_top'] + stroke_dict['f']
    word_g = stroke_dict['c_right'] + stroke_dict['j_like']
    word_h = stroke_dict['l_a_left'] + stroke_dict['n']
    word_i = stroke_dict['l_short_middle'] + stroke_dict['dot']
    word_j = stroke_dict['j']
    word_k = stroke_dict['l_a_left'] + stroke_dict['k']
    word_l = stroke_dict['l_a_middle']
    word_m = stroke_dict['m']
    word_n = stroke_dict['n']
    word_o = stroke_dict['o']
    word_p = stroke_dict['c_left'] + stroke_dict['l_b_left']
    word_q = stroke_dict['c_right'] + stroke_dict['l_b_right']
    word_r = stroke_dict['l_short_left'] + stroke_dict['r']
    word_s = stroke_dict['s']
    word_t = stroke_dict['line_top'] + stroke_dict['t']
    word_u = stroke_dict['u']
    word_v = stroke_dict['v']
    word_w = stroke_dict['w']
    word_x = stroke_dict['x']
    word_y = stroke_dict['y']
    word_z = stroke_dict['line_top'] + stroke_dict['z'] + stroke_dict['line_below']
    
    total_word_stroke_dict = {}
    total_word_stroke_dict['a'] = word_a
    total_word_stroke_dict['b'] = word_b
    total_word_stroke_dict['c'] = word_c
    total_word_stroke_dict['d'] = word_d
    total_word_stroke_dict['e'] = word_e
    total_word_stroke_dict['f'] = word_f
    total_word_stroke_dict['g'] = word_g
    total_word_stroke_dict['h'] = word_h
    total_word_stroke_dict['i'] = word_i
    total_word_stroke_dict['j'] = word_j
    total_word_stroke_dict['k'] = word_k
    total_word_stroke_dict['l'] = word_l
    total_word_stroke_dict['m'] = word_m
    total_word_stroke_dict['n'] = word_n
    total_word_stroke_dict['o'] = word_o
    total_word_stroke_dict['p'] = word_p
    total_word_stroke_dict['q'] = word_q
    total_word_stroke_dict['r'] = word_r
    total_word_stroke_dict['s'] = word_s
    total_word_stroke_dict['t'] = word_t
    total_word_stroke_dict['u'] = word_u
    total_word_stroke_dict['v'] = word_v
    total_word_stroke_dict['w'] = word_w
    total_word_stroke_dict['x'] = word_x
    total_word_stroke_dict['y'] = word_y
    total_word_stroke_dict['z'] = word_z

    print ("total word stroke dict: ", total_word_stroke_dict)
    return (total_word_stroke_dict)

def word_table():
    # (-1, -1) -> pen up
    single_word_dict = {}
    point_m = [(1,0), (3,0), (2,0), (1,1), (2,2), (3,2), (2,2), (1,3), (2,4), (3,4)]
    point_r = [(1,1), (3,1), (2,1), (1,2), (1,3)]
    point_e = [(2,1), (2,3), (1,3), (0,2), (1,1), (3,1), (4,2),(4,3)]
    point_h = [(0,1), (4,1), (3,1), (2,2), (3,3), (4,3)]
    #point_t = [(1,1), (1,3), (0, 2), (4,2), (3,3)]
    point_t = [(1,1), (1,3), (-1, -1), (0, 2), (4,2), (3,3)]
    point_n = [(1,1), (3,1), (2,1), (1,2), (2,3), (3,3)]
    point_a = [(1,3), (1,2), (2,1), (3,2), (2,3), (1,3), (3,3)]
    point_s = [(0,3), (0,2), (1,1), (2,2), (3,3), (4,2), (4,1)]
    point_d = [(2,3), (2,2), (3,1), (4,2), (4,3), (0,3)]
    point_u = [(1,1), (3,1), (3,2), (1,3), (2,3), (3,4)]
    point_o = [(1,2), (1,1), (3,1), (3,3), (1,3), (1,2)]
    point_l = [(0,2), (3,2)]
    point_c = [(1,3), (1,2), (2,1), (3,2), (3,3)]
    point_space = []

    single_word_dict['a'] = point_a
    single_word_dict['c'] = point_c
    single_word_dict['d'] = point_d
    single_word_dict['e'] = point_e
    single_word_dict['h'] = point_h
    single_word_dict['l'] = point_l
    single_word_dict['m'] = point_m
    single_word_dict['n'] = point_n
    single_word_dict['o'] = point_o
    single_word_dict['r'] = point_r
    single_word_dict['s'] = point_s
    single_word_dict['t'] = point_t
    single_word_dict['u'] = point_u
    single_word_dict[" "] = point_space
    return (single_word_dict)

def predict_img(shape):
    # test case: m
    img = new_img(shape)
    #point_m = [(1,0), (3,0), (2,0), (1,1), (2,2), (3,2), (2,2), (1,3), (2,4), (3,4)]
    #for i in range(0, len(point_m)):
    #    x = point_m[i][0]
    #    y = point_m[i][1]
    #    img[x,y,0] = 255
    savename = "./single_word/" + "m.png"
    cv2.imwrite(savename, img)

def all_stroke():
    words1 = "clouds and"
    words2 = "thunderstorms"
    words_list = [words1, words2]
    #print ("words list: ", words_list)
    single_word_dict = word_table()
    #len_words1 = len(words1)
    #len_words2 = len(words2)
    total_stroke = []
    ########### bug
    for k in range(0, len(words_list)):
        for i in range(0, len(words_list[k])):
            tmp_key = str(words_list[k][i])
            try:
                tmp_list = []
                stroke = single_word_dict[tmp_key]
                if (stroke == []):
                    pass
                else:
                    for j in range(0, len(stroke)):
                        tmp_point = []
                        stroke[j] = list(stroke[j])
                        if (stroke[j][0] == -1):
                            tmp_x = -1
                            tmp_y = -1
                        else:
                            tmp_x = int(stroke[j][0]) + int(k) * 7
                            tmp_y = int(stroke[j][1]) + int(i) * 5
                        tmp_point.append(tmp_x)
                        tmp_point.append(tmp_y)
                        tmp_list.append(tmp_point)
                    total_stroke.append(tmp_list)
            except:
                pass
    
    max_x = 0
    max_y = 0
    for ele in range(0, len(total_stroke)):
        for i in range(0, len(total_stroke[ele])):
            tmp_x = total_stroke[ele][i][0]
            tmp_y = total_stroke[ele][i][1]
            if (tmp_x > max_x):
                max_x = tmp_x
            if (tmp_y > max_y):
                max_y = tmp_y

    shape = (max_x+2, max_y+2, 3)
    img = new_img(shape)
    for stroke in range(0, len(total_stroke)):
        for point in range(0, len(total_stroke[stroke])):
            #print (total_stroke[stroke][point])
            point_x, point_y = total_stroke[stroke][point]
            if ((point_x == -1) or (point_y == -1)):
                pass
            else:
                img[point_x, point_y, 0] = img[point_x, point_y, 1] = img[point_x, point_y, 2] = 0
    savename = "./predict_point.png"
    cv2.imwrite(savename, img)
    return (total_stroke)


if __name__ == "__main__":
    #total_stroke = all_stroke()
    #print ("total stroke: ", total_stroke)
    
    stroke_dict = stroke_table()
    total_word_stroke_dict = word_stroke(stroke_dict)

