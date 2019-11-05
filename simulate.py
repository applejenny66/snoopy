#simulate.py

import numpy as np
import cv2
from utils import blankarray
class simulate():
    def __init__(self, sequence_array, times):
        self.sequence_array = sequence_array
        self.shape = self.sequence_array.shape
        self.times = times
    
    def simulatesequence(self):
        for time in range(1, self.times):
            new_img = blankarray(self.shape)
            for x in range(0, self.shape[0]):
                for y in range(0, self.shape[1]):
                    if (self.sequence_array[x, y, 0] == time):
                        new_img[x, y, 0] = new_img[x, y, 1] = new_img[x, y, 2] = 0
            savename = "./test/" + str(time) + ".png"
            cv2.imwrite(savename, new_img)

