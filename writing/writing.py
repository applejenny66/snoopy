import cv2 
import numpy as np
name = "cloud.png"
img = cv2.imread(name)
shape = img.shape
print (img.shape)
#crop_img = img[50:100, 20:200]
#cv2.imshow("cropped", crop_img)
#cv2.imshow("test", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


x_min = 0
y_min = 0
x_max = 0
y_max = 0
for x in range(0, shape[0]):
    if x_min != 0:
        break
    for y in range(0, shape[1]):
        if img[x][y][0] != 255:
            x_min = x
            break
for y in range(0, shape[1]):
    if y_min != 0:
        break
    for x in range(0, shape[0]):
        if img[x][y][0] != 255:
            y_min = y
            break
for x in range(shape[0]-1,-1,-1):
    if x_max != 0:
        break
    for y in range(shape[1]-1,-1,-1):
        if img[x][y][0] != 255:
            x_max = x
            break
for y in range(shape[1]-1,-1,-1):
    if y_max != 0:
        break
    for x in range(shape[0]-1,-1,-1):
        if img[x][y][0] != 255:
            y_max = y
            break
print(x_min,y_min,x_max,y_max)
crop_img = img[x_min:x_max+2,y_min:y_max+2]
cv2.imwrite("crop_imgage.png",crop_img)