# transfer.py

import cv2
import numpy as np
from matplotlib import pyplot as plt


def readimg(name):
    img = cv2.imread(name)
    return (img)

def grayimg(img, name):
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    name = "./test/" + name
    cv2.imwrite(name, img_gray)
    return (img_gray)

def showdistribution(img):
    plt.hist(img.ravel(),256,[0,256])
    plt.savefig("hist.png")
    #plt.show()
    #hist = cv2.calcHist([img],[0],None,[256],[0,256])

def blurredimg(img, kernel_size=10):    
    kernel = np.ones((kernel_size,kernel_size),np.float32)/(kernel_size*kernel_size)
    dst = cv2.filter2D(img,-1,kernel)
    cv2.imwrite('./test/blurred.png', dst)
    #cv2.imshow('dst', dst)
    return (dst)

def threshold(img, x1, x2):
    ret2, thresh = cv2.threshold(img,x1,x2,0) #127
    cv2.imwrite("./test/thrshold.png", thresh)
    return (ret2, thresh)

def kmeans(img, K = 3):
    Z = img.reshape((-1,3))
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    return (res2)


def drawContours(draw_img, thresh_img):
    contours, hierarchy = cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    img_contour = cv2.drawContours(draw_img, contours, -1, (0,255,0), 3)
    cv2.imwrite('./test/contour.png', img_contour)
    #cv2.imshow('contour',img_contour)
    return (img_contour)

def main():
    img = readimg('pikachu.jpg')
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blurred_hsv_img = blurredimg(hsv_img, 15)
    gray_hsv_img = cv2.cvtColor(blurred_hsv_img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("./test/gray_hsv_img.png", gray_hsv_img)
    ret2, thresh = threshold(gray_hsv_img,140,255)
    hsv_img_contour = drawContours(img, thresh)
    cv2.imwrite('./test/contour_hsv.png', hsv_img_contour)
    """
    img_gray = grayimg(img, 'img_gray.png')
    showdistribution(img_gray)
    blurred_img = blurredimg(img, 20)
    k3_img = kmeans(blurred_img, K = 3)
    k3_gray_img = grayimg(k3_img, 'k3_img.png')
    blurred_gray_img = cv2.cvtColor(blurred_img, cv2.COLOR_BGR2GRAY)
    #ret2, thresh = threshold(blurred_gray_img,150,255) #127
    ret2, thresh = threshold(k3_gray_img,140,255)
    img3_contour = drawContours(k3_img, thresh)
    cv2.imwrite('./test/contour3.png', img3_contour)
    """
    
    



#cv2.waitKey(0)
#cv2.destroyAllWindows()



if __name__ == "__main__":
    main()