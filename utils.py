# utils.py

import numpy as np
import cv2
import os

def clearall():
    import shutil
    shutil.rmtree('./test')
    os.mkdir('./test')

def blankarray(shape):
    array = np.zeros(shape)
    for x in range(0, shape[0]):
        for y in range(0, shape[1]):
            array[x, y, 0] = array[x, y, 1] = array[x, y, 2] = 255
    return (array)