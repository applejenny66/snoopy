#img_processing.py

import numpy as np
import cv2

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
    img = cv2.imread("./test/contour_hsv.png")
    crop_img, max_x, min_x, max_y, min_y, x_dev, y_dev = crop_img(img)
    drawboundingbox(img, max_x, max_y, min_x, min_y)
    downsample(crop_img)