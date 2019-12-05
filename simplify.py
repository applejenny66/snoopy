#simplify.py

import numpy as np
import cv2
#import cv
from transfer_test import kmeans
import matplotlib.pyplot as plt
from crawl_color import color_table
from color_transfer import classify_table
from gen_point import img_2_paint

def background_no(img):
    shape = img.shape
    ret,thresh = cv2.threshold(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),127,255,0)
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    area_list = []
    perimeter_list = []
    center_list = []
    for i in range(0, len(contours)):
        cnt = contours[i]
        M = cv2.moments(cnt)
        if (M['m00'] == 0):
            cx = int(M['m10'])
            cy = int(M['m01'])
        else:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
        center_list.append((cx, cy))
        area = cv2.contourArea(cnt)
        area_list.append(area)
        perimeter = cv2.arcLength(cnt,True)
        perimeter_list.append(perimeter)

        #epsilon = 0.02*perimeter
        #approx = cv2.approxPolyDP(cnt,epsilon,True)
        #imgnew1 = cv2.drawContours(img, approx, -1, (0,0,255), 3)

    #print ("center list:", center_list)
    #print ("area list: ", area_list)
    #print ("perimeter list: ", perimeter_list)
    max_area = max(area_list)
    max_index = area_list.index(max_area)
    #epsilon = 0.02 * (perimeter_list[max_index])s
    #approx = cv2.approxPolyDP(contours[max_index],epsilon,True)
    #object_img = cv2.drawContours(img, approx, -1, (0,0,255), 3)
    object_img = cv2.drawContours(img, contours[max_index], -1, (0,255,0), 3)

    for x in range(0, shape[0]):
        for y in range(0, shape[1]):
            pt = (y, x)
            val = cv2.pointPolygonTest(contours[max_index], pt, measureDist=False)
            if (val == -1):
                object_img[x, y, 0] = object_img[x, y, 1] = object_img[x, y, 2] = 255

    cv2.imwrite("./test/object_img.png", object_img)
    return (object_img)

def totalcolor(img):
    shape = img.shape
    r_list = []
    g_list = []
    b_list = []
    color_list = []
    for x in range(0, shape[0]):
        for y in range(0, shape[1]):
            tmp_color = [img[x, y, 0], img[x, y, 1], img[x, y, 2]]
            tmp_r = tmp_color[0]
            tmp_g = tmp_color[1]
            tmp_b = tmp_color[2]
            if (tmp_r in r_list):
                if (tmp_g in g_list):
                    if (tmp_b in b_list):
                        tmp_r_index = r_list.index(tmp_r)
                        tmp_g_index = g_list.index(tmp_g)
                        tmp_b_index = b_list.index(tmp_b)
                        if (tmp_r_index == tmp_g_index == tmp_b_index):
                            pass
                        else:
                            r_list.append(tmp_r)
                            g_list.append(tmp_g)
                            b_list.append(tmp_b)
                            color_list.append(tmp_color)

            elif (tmp_r not in r_list):
                if (tmp_g not in g_list):
                    if (tmp_b not in b_list):
                        r_list.append(tmp_r)
                        g_list.append(tmp_g)
                        b_list.append(tmp_b)
                        color_list.append(tmp_color)
    #print ("color list [0]: ", color_list[0])
    total_k = len(color_list)
    #print ("total color: ", len(color_list))
    return (total_k, r_list, g_list, b_list, color_list)

def takefourth(elem):
    return elem[3]

def colorclassify1(color_list):
    total_color_list = []
    for i in range(0, len(color_list)):
        #print ("color: ", color_list[i])
        tmp_list = []
        tmp_total = 0
        for j in range(0, 3):
            tmp_total += color_list[i][j]
        tmp_list.append(color_list[i][0])
        tmp_list.append(color_list[i][1])
        tmp_list.append(color_list[i][2])
        tmp_list.append(tmp_total)
        total_color_list.append(tmp_list)
    print ("total color list [0]: ", total_color_list[0])
    total_color_list.sort(key = takefourth)
    return (total_color_list)
    
def colorclassify2(total_color_list):
    dist_list = []
    for i in range(0, len(total_color_list)-1):
        tmp_list = []
        tmp_dist = 0
        for j in range(0, 3):
            tmp_dist += (total_color_list[i+1][j] - total_color_list[i][j])*\
                    (total_color_list[i+1][j] - total_color_list[i][j])
        tmp_list.append(i)
        tmp_list.append(tmp_dist)
        dist_list.append(tmp_list)
    return (dist_list)

def plotdist(dist_list):
    under_100_list = []
    under_300_list = []
    under_500_list = []
    under_700_list = []
    under_1000_list = []
    over_1000_list = []
    for i in range(0 ,len(dist_list)):
        if (dist_list[i][1] < 100):
            under_100_list.append(dist_list[i])
        elif (dist_list[i][1] < 300):
            under_300_list.append(dist_list[i])
        elif (dist_list[i][1] < 500):
            under_500_list.append(dist_list[i])
        elif (dist_list[i][1] < 700):
            under_700_list.append(dist_list[i])
        elif (dist_list[i][1] < 1000):
            under_1000_list.append(dist_list[i])
        else:
            over_1000_list.append(dist_list[i])
    data_list = [len(under_100_list), len(under_300_list), len(under_500_list), len(under_700_list)\
        , len(under_1000_list), len(over_1000_list)]
    data_name = ["100", "300", "500", "700", "1000", ">1000"]
    
    plt.figure(figsize=(9, 3))

    #plt.plot(131)
    plt.bar(data_name, data_list)
    plt.savefig("./test/bar.png")
    #plt.show()

def colorclassify3(dist_list, total_color_list):
    remove_list = []
    for i in range(0, len(dist_list)):
        # [index, dist]
        tmp_dist = dist_list[i][1]
        if (tmp_dist < 100):
            remove_list.append(dist_list[i][0])
    
    remove_list.sort(reverse=True)
    for j in range(0, len(remove_list)):
        indx = remove_list[j]
        total_color_list.remove(total_color_list[indx])
    return (total_color_list)

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

    save_name = "./test/test.png"
    cv2.imwrite(save_name, new_img)




if __name__ == "__main__":
    img = cv2.imread("./test/resized.png")
    
    object_img = background_no(img)
    bgr_img1 = cv2.cvtColor(object_img, cv2.COLOR_HSV2BGR)
    cv2.imwrite("./test/bgr_object.png", bgr_img1)
    painting_img = img_2_paint("./test/bgr_object.png")
    #cv2.imshow("1", bgr_img1)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    
    """
    total_k, r_list, g_list, b_list, color_list = totalcolor(object_img)
    #for i in range(0, 10):
    #    print (color_list[i])
    #print ("color list: ", color_list[0])
    total_color_list = colorclassify1(color_list)
    dist_list = colorclassify2(total_color_list)
    #for i in range(0, 10):
    #    print ("dist list : ", dist_list[i])
    #plotdist(dist_list)
    simple_total_color_list = colorclassify3(dist_list, total_color_list)
    print ("length of simple color: ", len(simple_total_color_list))
    k = len(simple_total_color_list)
    k_img = kmeans(object_img, K = k)
    bgr_img2 = cv2.cvtColor(k_img, cv2.COLOR_HSV2BGR)
    cv2.imwrite("./test/k_resized.png", bgr_img2)
    """
    np_color_table = cv2.imread("color_table.png")
    #np_color_table = color_table()
    table_size = np_color_table.shape
    #print (size)
    #(239, 3)
    black_table, r_table, g_table, b_table = classify_table(np_color_table)
    #shape = bgr_img2.shape
    compare_color(painting_img, black_table, r_table, g_table, b_table)
    #for i in range(0, 10):
    #    print (total_color_List[i])
    #k_decided = int(total_k / 100)
    #print (k_decided)
    #k_img = kmeans(object_img, K = k_decided)
    #bgr_img2 = cv2.cvtColor(k_img, cv2.COLOR_HSV2BGR)
    #cv2.imwrite("./test/k_resized.png", bgr_img2)

