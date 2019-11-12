#simplify.py

import numpy as np
import cv2
#import cv

def background_no(img):
    shape = img.shape
    ret,thresh = cv2.threshold(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),127,255,0)
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)#得到轮廓信息
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

        #轮廓的近似
        #epsilon = 0.02*perimeter
        #approx = cv2.approxPolyDP(cnt,epsilon,True)
        #imgnew1 = cv2.drawContours(img, approx, -1, (0,0,255), 3)

    print ("center list:", center_list)
    print ("area list: ", area_list)
    print ("perimeter list: ", perimeter_list)
    max_area = max(area_list)
    max_index = area_list.index(max_area)
    #epsilon = 0.02 * (perimeter_list[max_index])s
    #approx = cv2.approxPolyDP(contours[max_index],epsilon,True)
    #object_img = cv2.drawContours(img, approx, -1, (0,0,255), 3)
    object_img = cv2.drawContours(img, contours[max_index], -1, (0,255,0), 3)#把所有轮廓画出来

    for x in range(0, shape[0]):
        for y in range(0, shape[1]):
            pt = (y, x)
            val = cv2.pointPolygonTest(contours[max_index], pt, measureDist=False)
            if (val == -1):
                object_img[x, y, 0] = object_img[x, y, 1] = object_img[x, y, 2] = 255

    cv2.imwrite("./test/object_img.png", object_img)


if __name__ == "__main__":
    img = cv2.imread("./test/resized.png")
    background_no(img)