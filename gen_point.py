#!/usr/bin/env python

import time
import cv2
import numpy as np
import csv
import os
import sys
import shutil

from crawl_color import color_table
from color_transfer import classify_table

def img_2_paint(img):
    img = cv2.imread(img)
    # shape = (217, 403, 3) -> 21.7 cm, 40.3 cm, rgb 3 colors
    shape = img.shape
    new_shape = (int(shape[0]/10), int(shape[1]/10), 3)
    print (new_shape)
    new_img = np.zeros(new_shape)
    tmp_total_r = 0
    tmp_total_g = 0
    tmp_total_b = 0
    for i in range(0, new_shape[0]):
        for j in range(0, new_shape[1]):
            for w in range(0, 10):
                for h in range(0, 10):
                    tmp_total_r += img[i*10+w, j*10+h, 0]
                    tmp_total_g += img[i*10+w, j*10+h, 1]
                    tmp_total_b += img[i*10+w, j*10+h, 2]
            tmp_total_r = int(tmp_total_r / 100)
            tmp_total_g = int(tmp_total_g / 100)
            tmp_total_b = int(tmp_total_b / 100)
            new_img[i, j, 0] = tmp_total_r
            new_img[i, j, 1] = tmp_total_g
            new_img[i, j, 2] = tmp_total_b
    savename = "./test/painting.png"
    cv2.imwrite(savename, new_img)
    print ("finished")
    print ("shape: ", new_img.shape)
    return (new_img)

def compare_color(img, bl_table, r_table, g_table, b_table):
    new_img = img.copy()
    #print (new_img[10, 10])
    shape = img.shape
    bl_len = len(bl_table)
    r_len = len(r_table)
    g_len = len(g_table)
    b_len = len(b_table)
    for x in range(0, shape[0]):
        for y in range(0, shape[1]):
            tmp_color = (img[x, y, 2], img[x, y, 1], img[x, y, 0]) #(b, g, r)
            #print (tmp_color)
            if (tmp_color[0] == tmp_color[1] == tmp_color[2]):
                dev_list = []
                for i in range(0, bl_len):
                    dev = 0
                    for p in range(0, 3):
                        dev += (abs(tmp_color[p] - bl_table[i][p])*abs(tmp_color[p] - bl_table[i][p]))
                    dev_list.append(dev)
                dev_min = min(dev_list)
                dev_index = dev_list.index(dev_min)
                new_color = (bl_table[dev_index][0], bl_table[dev_index][1], bl_table[dev_index][2])
            
            else:
                tmp_max = max(tmp_color)
                tmp_index = int(tmp_color.index(tmp_max))
                #print ("tmp index: ", tmp_index)
                if (tmp_index == 2): #b
                    dev_list = []
                    for i in range(0, b_len):
                        dev = 0
                        for p in range(0, 3):
                            dev += (abs(tmp_color[p] - b_table[i][p])*abs(tmp_color[p] - b_table[i][p]))
                        dev_list.append(dev)
                    dev_min = min(dev_list)
                    dev_index = dev_list.index(dev_min)
                    new_color = (b_table[dev_index][0], b_table[dev_index][1], b_table[dev_index][2])
                    #print ("dev list: ", dev_list)
                elif (tmp_index == 1): #g
                    dev_list = []
                    for i in range(0, g_len):
                        dev = 0
                        for p in range(0, 3):
                            dev += (abs(tmp_color[p] - g_table[i][p])*abs(tmp_color[p] - g_table[i][p]))
                        dev_list.append(dev)
                    dev_min = min(dev_list)
                    dev_index = dev_list.index(dev_min)
                    new_color = (g_table[dev_index][0], g_table[dev_index][1], g_table[dev_index][2])
                else:
                    dev_list = []
                    for i in range(0, r_len):
                        dev = 0
                        for p in range(0, 3):
                            dev += (abs(tmp_color[p] - r_table[i][p])*abs(tmp_color[p] - r_table[i][p]))
                        dev_list.append(dev)
                    dev_min = min(dev_list)
                    dev_index = dev_list.index(dev_min)
                    new_color = (r_table[dev_index][2], r_table[dev_index][1], r_table[dev_index][0])
                new_img[x, y, 0], new_img[x, y, 1], new_img[x, y, 2] = new_color[0], new_color[1], new_color[2]

    save_name = "./test/final.png"
    cv2.imwrite(save_name, new_img)

def takeFour(elem):
    return elem[3]

def paint_2_csv(img):
    img = cv2.imread(img)
    shape = img.shape
    print ("painting shape: ", shape)
    color_r = []
    color_g = []
    color_b = []
    total_color = []
    for x in range(0, shape[0]):
        for y in range(0, shape[1]):
            tmp_list = []
            tmp_total = 0
            tmp_color = img[x, y]
            tmp_r = int(tmp_color[0])
            tmp_g = int(tmp_color[1])
            tmp_b = int(tmp_color[2])
            tmp_total = tmp_r + tmp_g + tmp_b
            tmp_list.append(tmp_r)
            tmp_list.append(tmp_g)
            tmp_list.append(tmp_b)
            tmp_list.append(tmp_total)
            if (tmp_r not in color_r):
                color_r.append(tmp_r)
                color_g.append(tmp_g)
                color_b.append(tmp_b)
                total_color.append(tmp_list)
            else:
                if (tmp_g not in color_g):
                    color_r.append(tmp_r)
                    color_g.append(tmp_g)
                    color_b.append(tmp_b)
                    total_color.append(tmp_list)
                else:
                    if (tmp_b not in color_b):
                        color_r.append(tmp_r)
                        color_g.append(tmp_g)
                        color_b.append(tmp_b)
                        total_color.append(tmp_list)
                    else:
                        index_r = int(color_r.index(tmp_r))
                        index_g = int(color_g.index(tmp_g))
                        index_b = int(color_b.index(tmp_b))
                        if (index_r == index_g == index_b):
                            pass
                        else:
                            if ((color_r[index_r] == tmp_r) and (color_g[index_r] == tmp_g) \
                                and (color_b[index_r] == tmp_b)):
                                pass
                            elif ((color_r[index_g] == tmp_r) and (color_g[index_g] == tmp_g) \
                                and (color_b[index_g] == tmp_b)):
                                pass
                            elif ((color_r[index_b] == tmp_r) and (color_g[index_b] == tmp_g) \
                                and (color_b[index_b] == tmp_b)):
                                pass
                            else:
                                color_r.append(tmp_r)
                                color_g.append(tmp_g)
                                color_b.append(tmp_b)
                                total_color.append(tmp_list)
                            
                            #    if ()
                            #    (color_r[index_r] == color_g[index_b]) or \
                            #    (color_r[index_b] == color_g[index_g])):

                            #color_r.append(tmp_r)
                            #color_g.append(tmp_g)
                            #color_b.append(tmp_b)
                            #total_color.append(tmp_list)
    total_number = len(color_r)
    total_color.sort(key=takeFour)
    
    print ("total color number: ", total_number)
    print ("first color: ", total_color[1])
    print ("second color: ", total_color[2])



    
    path = "./painting"
    try:
        if os.path.exists('./painting'):
            shutil.rmtree(path)
        os.mkdir(path)
    except:
        print ("dir exist")
    
    for i in range(0, total_number):
        name = path + "/" + str(i) + ".csv"
        color_r = total_color[i][0]
        color_g = total_color[i][1]
        color_b = total_color[i][2]
        with open(name, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([color_r, color_g, color_b])
            for x in range(0, shape[0]):
                for y in range(0, shape[1]):
                    if ((img[x, y, 0] == color_r) and (img[x, y, 1] == color_g) and \
                        (img[x, y, 2] == color_b)):
                        writer.writerow([x, y])

    
    """
    name = "painting1.csv"
    # name = path + "painting1.csv"
    with open(name, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Spam'] * 5 + ['Baked Beans'])
        writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])           
    """
if __name__ == "__main__":
    np_color_table = color_table()
    size = np_color_table.shape
    bl_table, r_table, g_table, b_table = classify_table(np_color_table)

    new_img = img_2_paint("./test/bgr_object.png")
    compare_color(new_img, bl_table, r_table, g_table, b_table)

    paint_2_csv("./test/final.png")