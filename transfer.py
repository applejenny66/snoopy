# transfer.py

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("pikachu.jpg", 0)
#plt.hist(img.ravel(),256,[0,256]); plt.show()
#hist = cv2.calcHist([img],[0],None,[256],[0,256])
#print (type(hist))
#print (hist.shape) (256, 1)

#dev_hist = []

#for i in range(0, 255):
#    tmp_dev = abs(hist[i+1] - hist[i])
#    dev_hist.append(tmp_dev)

#max_pixel = max(dev_hist)
#max_index = dev_hist.index(max_pixel)

#dev_hist.remove(max_pixel)
#second_max_pixel = max(dev_hist)
#second_index = dev_hist.index(second_max_pixel)
#min_pixel = min(dev_hist)
#print (max_pixel, max_index, second_max_pixel, second_index)
#img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


kernel = np.ones((10,10),np.float32)/100
dst = cv2.filter2D(img,-1,kernel)
#cv2.imshow('dst', dst)
img_gray = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
ret2,thresh2 = cv2.threshold(img_gray,100,255,0) #127
print (type(thresh2))
print (thresh2.shape)
cv2.imshow('thresh2', thresh2)

Z = img.reshape((-1,3))
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 3
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))
#print (type(ret), type(label), type(center))
#cv2.imshow('thresh2', res2)



# Now convert back into uint8, and make original image


contours, hierarchy = cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img_contour = cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow('contour',img_contour)

cv2.waitKey(0)
cv2.destroyAllWindows()
