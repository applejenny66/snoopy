import cv2 
import numpy as np

#crop_img = img[50:100, 20:200]
#cv2.imshow("cropped", crop_img)
#cv2.imshow("test", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

def findwords():
    name = "cloud.png"
    img = cv2.imread(name)
    shape = img.shape
    print (img.shape)
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
    cv2.imwrite("crop_img.png",crop_img)

def binary():
    img = cv2.imread("crop_img.png")
    new_img = img.copy()
    shape = img.shape
    for x in range(0, shape[0]):
        for y in range(0, shape[1]):
            if (img[x, y, 0] != 255):
                new_img[x, y, 0] = new_img[x, y, 1] = new_img[x, y, 2] = 0
            else:
                new_img[x, y, 0] = new_img[x, y, 1] = new_img[x, y, 2] = 255
    cv2.imwrite("binary.png", new_img)

def classifywords():
    img = cv2.imread("binary.png")
    shape = img.shape
    print ("shape: ", shape) #(11, 40, 3)
    first_x = 0
    x_list = []
    y_list = []
    for y in range(0, shape[1]):
        if (first_x != 0):
            break
        for x in range(0, shape[0]):
            if (img[x, y, 0] == 0):
                first_x = x
                break
    for y in range(0, shape[1]):
        for x in range(0, shape[0]):
            pass

                

if __name__ == "__main__":
    findwords()
    binary()
    classifywords()
                