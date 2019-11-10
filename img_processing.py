#img_processing.py

import numpy as np
import cv2

img = cv2.imread("pikachu.jpg")
print ("img shape: ", img.shape)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imwrite("./test/hsv_pikachu.png", hsv_img)
gray_hsv_img = cv2.cvtColor(hsv_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray_hsv.png", gray_hsv_img)
print ("type hsv img: ", type(hsv_img))
shape = hsv_img.shape
print ("shape: ", shape)
#for x in range(0, shape[0]):
#    for y in range(0, shape[1]):
