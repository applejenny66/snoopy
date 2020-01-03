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
    #c
    stroke_c_right = []
    for i in range(-20, 5):
        tmp_list = []
        tmp_angle = i * pi / 16
        tmp_x = round(2 + cos(tmp_angle), 3)
        tmp_y = round(1 + sin(tmp_angle), 3)
        tmp_list.append(tmp_x)
        tmp_list.append(tmp_y)
        stroke_c_right.append(tmp_list)
        #print (i, ": ", tmp_list)
    #print ("test: ", cos(pi), sin(pi))
    print ("stroke c: ", stroke_c_right)

    # c <-
    stroke_c_left = []
    for i in range(20, -5, -1):
        tmp_list = []
        tmp_angle = i * pi / 16
        tmp_x = round(2 + cos(tmp_angle), 3)
        tmp_y = round(1 + sin(tmp_angle), 3)
        tmp_list.append(tmp_x)
        tmp_list.append(tmp_y)
        stroke_c_left.append(tmp_list)
        print (i, ": ", tmp_list)

    # r
    stroke_r = []
    for i in range(24, 11, -1):
        tmp_list = []
        tmp_angle = i * pi / 16
        tmp_x = round(2 + cos(tmp_angle), 3)
        tmp_y = round(1 + sin(tmp_angle), 3)
        tmp_list.append(tmp_x)
        tmp_list.append(tmp_y)
        stroke_r.append(tmp_list)
    
    # half-circle (open below)
    stroke_half_cirle_below = []
    for i in range(24, 7, -1):
        tmp_list = []
        tmp_angle = i * pi / 16
        tmp_x = round(2 + cos(tmp_angle), 3)
        tmp_y = round(1 + sin(tmp_angle), 3)
        tmp_list.append(tmp_x)
        tmp_list.append(tmp_y)
        stroke_half_cirle_below.append(tmp_list)
        stroke_half_cirle_below.append([4, 2])

    # o
    stroke_o = []
    for i in range(24, -9, -1):
        tmp_list = []
        tmp_angle = i * pi / 16
        tmp_x = round(2 + cos(tmp_angle), 3)
        tmp_y = round(1 + sin(tmp_angle), 3)
        tmp_list.append(tmp_x)
        tmp_list.append(tmp_y)
        stroke_o.append(tmp_list)

    # .
    stoke_dot = [[1,1]]

    # -
    stroke_line_top = [[2, 0], [2, 2]]
    stroke_line_middle = [[3, 0], [3, 2]]
    stroke_line_below = [[4, 0], [4, 2]]

    # l
    stroke_l_a_left = [[0, 0], [4, 0]]
    stroke_l_a_middle = [[0, 1], [4, 1]]
    stroke_l_a_right = [[0, 2], [4, 2]]
    stroke_l_b_left = [[2, 0], [6, 0]]
    stroke_l_b_right = [[2, 2], [6, 2]]
    stroke_l_short_left = [[2, 0], [4, 0]]
    stroke_l_short_middle = [[2, 1], [4, 1]]
    stroke_l_short_right = [[2, 2], [4, 2]]
    
    # k
    stroke_k = [[2,2], [3, 0], [4, 2]]

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
    stroke_table()


