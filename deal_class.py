#deal_class.py

import numpy as np
import cv2
from dealing import dealing
from simulate import simulate
from utils import clearall

def read_img(name):
    img = cv2.imread(name)
    return (img)
    #shape = img.shape

def get_shape(img):
    shape = img.shape
    return (shape)

def new_array(shape):
    array = np.zeros(shape)
    return (array)

def get_point(img, shape, array):
    count = 0
    for x in range(0, shape[0]):
        for y in range(0, shape[1]):
            if (img[x,y,0] >= 100):
                pass
            else:
                array[x, y, 0] = array[x, y, 1] = array[x, y, 2] = 255
                count += 1
    print ("total point: ", count)
    return (array)

def saveimg(array, name):
    cv2.imwrite(name, array)

def main():
    clearall()
    img = read_img('snoopy_cut.png')
    img_shape = get_shape(img)
    point_array = new_array(img_shape)
    point_array = get_point(img, img_shape, point_array)
    cv2.imwrite("snoopy_binary.png", point_array)
    print ("finished saving img")
    deal = dealing(point_array)
    sequence, painted, times = deal.ifline()[0], deal.ifline()[1], deal.ifline()[2]
    print ("times: ", times)
    simulation = simulate(sequence, times)
    simulation.simulatesequence()

if __name__ == "__main__":
    main()
    