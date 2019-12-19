# color_transfer.py
from crawl_color import color_table
import cv2
import numpy as np

bgr_img = cv2.imread("./test/k_resized.png")
shape = bgr_img.shape

def classify_table(color_table):
    shape = color_table.shape
    red_table = []
    green_table = []
    blue_table = []
    black_table = []
    for i in range(0, shape[0]):
        tmp_list = []
        tmp_r = color_table[i, 0] #color_table[i, 0, 0]
        tmp_g = color_table[i, 1]
        tmp_b = color_table[i, 2]
        tmp_list.append(tmp_r)
        tmp_list.append(tmp_g)
        tmp_list.append(tmp_b)
        #print ("tmp list: ", tmp_list)
        if (tmp_list[0] == tmp_list[1] == tmp_list[2]):
            black_table.append(i)
        else:
            max_val = max(tmp_list)
            max_index = int(tmp_list.index(max_val))
            if (max_index == 0):
                red_table.append(i)
            elif (max_index == 1):
                green_table.append(i)
            elif (max_index == 2):
                blue_table.append(i)
            else:
                print ("error")
    black_len = len(black_table)
    r_len = len(red_table)
    g_len = len(green_table)
    b_len = len(blue_table)
    
    dtype = [('R', int), ('G', int), ('B', int)]
    bl_table = np.zeros((black_len), dtype=dtype)
    r_table = np.zeros((r_len), dtype=dtype)
    g_table = np.zeros((g_len), dtype=dtype)
    b_table = np.zeros((b_len), dtype=dtype)
    for i in range(0, black_len):
        bl_table[i] = color_table[black_table[i], 0], color_table[black_table[i], 1], color_table[black_table[i], 2]

    for i in range(0, r_len):
        r_table[i] = color_table[red_table[i], 0], color_table[red_table[i], 1], color_table[red_table[i], 2]
    for i in range(0, g_len):
        g_table[i] = color_table[green_table[i], 0], color_table[green_table[i], 1], color_table[green_table[i], 2]
    for i in range(0, b_len):
        b_table[i] = color_table[blue_table[i], 0], color_table[blue_table[i], 1], color_table[blue_table[i], 2]
    bl_table = np.sort(bl_table, order = 'R')
    r_table = np.sort(r_table, order = 'R')
    g_table = np.sort(g_table, order = 'G')
    b_table = np.sort(b_table, order = 'B')
    #print ("red table: ", r_table)
    #print ("green table: ", g_table)
    #print ("blue table: ", b_table)
    return (bl_table, r_table, g_table, b_table)


if __name__ == "__main__":
    np_color_table = color_table()
    #print (np_color_table)
    size = np_color_table.shape
    #print (size)
    #(239, 3)
    bl_table, r_table, g_table, b_table = classify_table(np_color_table)
    
    """
    for x in range(0, shape[0]):
        for y in range(0, shape[1]):
            tmp_color = (bgr_img[x, y, 0], bgr_img[x, y, 1], bgr_img[x, y, 2])
            print (tmp_color)
    """