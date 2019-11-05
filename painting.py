#painting.py

import numpy as np
import cv2

class painting():
    def __init__(self, img):
        self.img = img
        self.shape = self.img.shape

    def 