#test.py
import cv2 
import numpy as np
import os
import csv

def word_table():
    # (-1, -1) -> pen up
    single_word_dict = {}
    point_m = [(1,0), (3,0), (2,0), (1,1), (2,2), (3,2), (2,2), (1,3), (2,4), (3,4)]
    point_r = [(1,1), (3,1), (2,1), (1,2), (1,3)]
    point_e = [(2,1), (2,3), (1,3), (0,2), (1,1), (3,1), (4,2),(4,3)]
    point_h = [(0,1), (4,1), (3,1), (2,2), (3,3), (4,3)]
    point_t = [(1,1), (1,3), (0, 2), (4,2), (3,3)]
    #point_t = [(1,1), (1,3), (-1, -1), (0, 2), (4,2), (3,3)]
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


if __name__ == "__main__":
    single_word_dict = word_table()
    x = single_word_dict[" "]
    print ("x: ", x)