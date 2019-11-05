# deal with snoopy
# deal.py
import numpy as np
import cv2

img = cv2.imread('snoopy_cut.png') 
shape = img.shape
point_array = np.zeros(shape)
count = 0

print ("shape: ", img.shape) #(150, 115, 3)
for x in range(0, shape[0]):
    for y in range(0, shape[1]):
        if (img[x,y,0] >= 100):
            pass
        else:
            point_array[x, y, 0] = point_array[x, y, 1] = point_array[x, y, 2] = 255
            count += 1
    
print ("total point: ", count)
cv2.imwrite("snoopy_binary.png", point_array)

print ("finished")