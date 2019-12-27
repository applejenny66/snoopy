import cv2 
import numpy as np
import os

#clouds and
# thunderstorms

def stroke():
    for filename in os.listdir("./sort_painting/"):
        #print (filename)
        name = "./sort_painting/" + filename
        print (name)
        img = cv2.imread(name)
        



if __name__ == "__main__":
    stroke()