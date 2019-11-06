# dealing.py

import numpy as np
import cv2

class dealing():
    def __init__(self, point):
        self.point = point #array
        self.shape = self.point.shape

    def ifline(self):
        new_array = np.zeros(self.shape)
        painted_array = np.zeros(self.shape)
        count = 1
        for x in range(0, self.shape[0]):
            if (x%5 == 0):
                print ("x now: ", x)
            for y in range(0, self.shape[1]):
                if (self.point[x, y, 0] == 0):
                    pass
                else:
                    new_array[x, y, 0] = count
                    if (painted_array[x, y, 0] != 0):
                        pass
                    else:
                        painted_array[x, y, 0] = 1
                        for w in range(-1, 1):
                            for h in range(-1, 1):
                                if (x+w > self.shape[0]-1 or x+w < 0 or\
                                    y+h > self.shape[1]-1 or y+h < 0):
                                    print ("over the img")
                                    pass
                                else:
                                    if (self.point[x+w, y+h, 0] == 0):
                                        pass
                                    else:
                                        new_array[x+w, y+h, 0] = count
                                        painted_array[x+w, y+h, 0] = 1
                                        """
                                        tmp = 1
                                        while tmp == 1:
                                            tmp_count = 0
                                            for ww in range(-1, 1):
                                                for hh in range(-1, 1):
                                                    if (x+w+ww > self.shape[0]-1 or x+w+ww < 0 or\
                                                        y+h+hh > self.shape[1]-1 or y+h+hh < 0):
                                                        pass
                                                    else:
                                                        if (self.point[x+w+ww, y+h+hh, 0] == 0):
                                                            pass
                                                        else:
                                                            new_array[x+w+ww, y+h+hh, 0] = count
                                                            painted_array[x+w+ww, y+h+hh, 0] = 1
                                                            tmp_count += 1
                                                    if (ww == 1 and hh == 1):
                                                        tmp = 0
                                            if (tmp_count == 0):
                                                tmp = 0
                                        """
                        count += 1
        self.painted_array = painted_array
        self.new_array = new_array
        return (new_array, painted_array, count)

    def simply(self, new_array):
        for x in range(0, self.shape[0]):
            for y in range(0, self.shape[1]):
                tmp_center = self.new_array[x, y, 0]
                if (tmp_center == 0):
                    pass
                else:
                    for w in range(-1, 1):
                        for h in range(-1, 1):
                            if (self.new_array[x+w, y+h, 0] == 0):
                                pass
                            else:
                                tmp_neighbor = self.new_array[x+w, y+h, 0]
                                if (tmp_neighbor > tmp_center):
                                    self.new_array[x+w, y+h, 0] = tmp_center
                                else:
                                    pass
        return (self.new_array)

    def showresult(self, array):
        tmp_list = []
        for x in range(0, self.shape[0]):
            for y in range(0, self.shape[1]):
                if (array[x, y, 0] != 0 and array[x, y, 0] not in tmp_list):
                    tmp_list.append(array[x, y, 0])
        return (tmp_list)
                        
