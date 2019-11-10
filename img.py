#img.py

import numpy as np
import cv2
from matplotlib import pyplot as plt

class img():
    def __init__(self, name):
        self.name = name
        self.img = cv2.imread(self.name)
        self.gray_img = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)

    def others(self):
        pass