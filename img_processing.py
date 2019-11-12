#img_processing.py

import numpy as np
import cv2

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
                object_img[x, y, 0] = object_img[x, y, 1] = object_img[x, y, 2] = 0

    cv2.imwrite("./test/object_img.png", object_img)

def crop_img(img):
    shape = img.shape
    x_list = []
    y_list = []
    for x in range(0, shape[0]):
        for y in range(0, shape[1]):
            tmp_g = int(img[x, y, 1])
            if (tmp_g == 255):
                x_list.append(x)
                y_list.append(y)
    min_x = min(x_list)
    min_y = min(y_list)
    max_x = max(x_list)
    max_y = max(y_list)
    x_dev = int(max_x - min_x)
    y_dev = int(max_y - min_y)
    crop_img = img[min_x:max_x+1, min_y:max_y+1]
    cv2.imwrite("./test/cropped_img.png", crop_img)
    return (crop_img, max_x, min_x, max_y, min_y, x_dev, y_dev)

def drawboundingbox(img, max_x, max_y, min_x, min_y):
    img2 = img.copy()
    for y in range(min_y, max_y+1):
        img2[min_x, y, 0] = img2[min_x, y, 1] = 0
        img2[min_x, y, 2] = 255
        img2[max_x, y, 0] = img2[max_x, y, 1] = 0
        img2[max_x, y, 2] = 255
    for x in range(min_x, max_x+1):
        img2[x, min_y, 0] = img2[x, min_y, 1] = 0
        img2[x, min_y, 2] = 255
        img2[x, max_y, 0] = img2[x, max_y, 1] = 0
        img2[x, max_y, 2] = 255
    cv2.imwrite("./test/boundingbox.png", img2)

def downsample(img):
    shape = img.shape
    width = shape[0]
    height = shape[1]
    if (width > height):
        max_para = width
    else:
        max_para = height
    scale = int(max_para / 500) + 1
    new_width = int(width / scale)
    new_height = int(height / scale)
    print (new_width, new_height)
    new_img = cv2.resize(img, (new_height, new_width), interpolation = cv2.INTER_AREA)
    cv2.imwrite("./test/resized.png", new_img)

if __name__ == "__main__":
    #img = cv2.imread("./test/blurred.png")
    #background_no(img)

    img = cv2.imread("./test/contour_hsv.png")
    crop_img, max_x, min_x, max_y, min_y, x_dev, y_dev = crop_img(img)
    img = cv2.imread("./test/blurred.png")
    origin_crop_img = img.copy()[min_x:max_x+1, min_y:max_y+1]
    cv2.imwrite("./test/origin_crop.png", origin_crop_img)
    drawboundingbox(img, max_x, max_y, min_x, min_y)
    #downsample(crop_img)
    downsample(origin_crop_img)