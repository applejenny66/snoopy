import cv2 
import numpy as np
import os
import csv

#clouds and
# thunderstorms

def new_img():
    shape = (5,5,1)
    img = np.zeros((shape))
    return (img)

def word_table():
    # (-1, -1) -> pen up
    single_word_dict = {}
    point_m = [(1,0), (3,0), (2,0), (1,1), (2,2), (3,2), (2,2), (1,3), (2,4), (3,4)]
    point_r = [(1,1), (3,1), (2,1), (1,2), (1,3)]
    point_e = [(2,1), (2,3), (1,3), (0,2), (1,1), (3,1), (4,2),(4,3)]
    point_h = [(0,1), (4,1), (3,1), (2,2), (3,3), (4,3)]
    point_t = [(1,1), (1,3), (-1, -1), (0, 2), (4,2), (3,3)]
    point_n = [(1,1), (3,1), (2,1), (1,2), (2,3), (3,3)]
    point_a = [(1,3), (1,2), (2,1), (3,2), (2,3), (1,3), (3,3)]
    point_s = [(0,3), (0,2), (1,1), (2,2), (3,3), (4,2), (4,1)]
    point_d = [(2,3), (2,2), (3,1), (4,2), (4,3), (0,3)]
    point_u = [(1,1), (3,1), (3,2), (1,3), (2,3), (3,4)]
    point_o = [(1,2), (1,1), (3,1), (3,3), (1,3), (1,2)]
    point_l = [(0,2), (3,2)]
    point_c = [(1,3), (1,2), (2,1), (3,2), (3,3)]

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
    return (single_word_dict)

def write_img(img):
    # test case: m
    point_m = [(1,0), (3,0), (2,0), (1,1), (2,2), (3,2), (2,2), (1,3), (2,4), (3,4)]
    for i in range(0, len(point_m)):
        x = point_m[i][0]
        y = point_m[i][1]
        img[x,y,0] = 255
    savename = "./single_word/" + "m.png"
    cv2.imwrite(savename, img)

def main():
    words1 = "clouds and"
    words2 = "thunderstorms"
    single_word_dict = word_table()
    len_words1 = len(words1)
    len_words2 = len(words2)
    max_len = max(len_words1, len_words2)
    print ("max_len: ", max_len)
    row = 2
    row_size = int(5 * row)
    column_size = int(5 * max_len)
    shape = (row_size, column_size, 1)
    print ("shape: ", shape)
    img = np.zeros((shape))

    for i in range(0, len(words1)):
        tmp_key = str(words1[i])
        try:
            tmp_point = single_word_dict[tmp_key]
            print ("word: ", tmp_key, tmp_point)
        except:
            print (tmp_key, "no words")



if __name__ == "__main__":
    main()
    
    #print ("word1 length: ", len(words1))
    #print ("c: ", tmp_c)
    #img = new_img()
    #write_img(img)