import numpy
import argparse
import cv2

image = cv2.imread('pikachu.jpg')
cv2.imshow("Original", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

eq = cv2.equalizeHist(gray)
##cv2.imshow("Gray EQ", eq)

#display two images in a figure
cv2.imshow("Histogram Equalization", numpy.hstack([gray, eq]))

cv2.imwrite("pikachu_eq.jpg", numpy.hstack([gray, eq]))


if(cv2.waitKey(0)==27):
    cv2.destroyAllWindows()
