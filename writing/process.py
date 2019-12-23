import cv2 
import numpy as np
import os


def singlewords():
    name = "binary.png"
    img = cv2.imread(name)
    shape = img.shape
    print ("shape: ", shape)
    #new_img = img.copy()
    position_array = np.zeros((shape))
    count  = 1
    for x in range(0, shape[0]):
        for y in range(0, shape[1]):
            if (img[x, y, 0] == 0):
                position_array[x, y, 0] =  count
                count += 1

    
    #### test
    for y in range(0, shape[1]):
        for x in range(0, shape[0]):
            if (position_array[x, y, 0] != 0):
                tmp_list = []
                if (y+1 <= shape[1]-1):
                    if (position_array[x, y+1, 0] != 0):
                        tmp_list.append(position_array[x, y, 0])
                        tmp_list.append(position_array[x, y+1, 0])
                        if (x+1 <= shape[0]-1):
                            if (position_array[x+1, y, 0] != 0):
                                tmp_list.append(position_array[x+1, y, 0])
                                if (position_array[x+1, y+1, 0] != 0):
                                    tmp_list.append(position_array[x+1, y+1, 0])
                                    min_index = min(tmp_list)
                                    position_array[x, y, 0] = position_array[x, y+1, 0] = \
                                    position_array[x+1, y, 0] = position_array[x+1, y+1, 0] = min_index
                                else:
                                    min_index = min(tmp_list)
                                    position_array[x, y, 0] = position_array[x, y+1, 0] = \
                                    position_array[x+1, y, 0] = min_index
                            else:
                                min_index = min(tmp_list)
                                position_array[x, y, 0] = position_array[x, y+1, 0] = min_index
                        else:
                            min_index = min(tmp_list)
                            position_array[x, y, 0] = position_array[x, y+1, 0] = min_index
                if (x+1 <= shape[0]-1):
                    tmp_list = []
                    if (position_array[x+1, y, 0] != 0):
                        tmp_list.append(position_array[x, y, 0])
                        tmp_list.append(position_array[x+1, y, 0])
                        if (y+1 <= shape[1]-1):
                            if (position_array[x, y+1, 0] != 0):
                                tmp_list.append(position_array[x, y+1, 0])
                                if (position_array[x+1, y+1, 0] != 0):
                                    tmp_list.append(position_array[x+1, y+1, 0])
                                    min_index = min(tmp_list)
                                    position_array[x, y, 0] = position_array[x, y+1, 0] = \
                                    position_array[x+1, y, 0] = position_array[x+1, y+1, 0] = min_index
                                else:
                                    min_index = min(tmp_list)
                                    position_array[x, y, 0] = position_array[x+1, y, 0] = \
                                    position_array[x, y+1, 0] = min_index
                            else:
                                min_index = min(tmp_list)
                                position_array[x, y, 0] = position_array[x+1, y, 0] = min_index
                        else:
                            min_index = min(tmp_list)
                            position_array[x, y, 0] = position_array[x+1, y, 0] = min_index
    
    #### test


    for y in range(0, shape[1]):
        for x in range(0, shape[0]):
            if (position_array[x, y, 0] != 0):
                tmp_list = []
                if (y+1 <= shape[1]-1):
                    if (position_array[x, y+1, 0] != 0):
                        tmp_list.append(position_array[x, y, 0])
                        tmp_list.append(position_array[x, y+1, 0])
                        min_index = min(tmp_list)
                        position_array[x, y, 0] = position_array[x, y+1, 0] = min_index
                if (x+1 <= shape[0]-1):
                    tmp_list = []
                    if (position_array[x+1, y, 0] != 0):
                        tmp_list.append(position_array[x, y, 0])
                        tmp_list.append(position_array[x+1, y, 0])
                        min_index = min(tmp_list)
                        position_array[x, y, 0] = position_array[x+1, y, 0] = min_index
    
    for x in range(0, shape[0]):
        for y in range(0, shape[1]):
            if (position_array[x, y, 0] != 0):
                tmp_list = []
                if (x+1 <= shape[0]-1):
                    if (position_array[x+1, y, 0] != 0):
                        tmp_list.append(position_array[x, y, 0])
                        tmp_list.append(position_array[x+1, y, 0])
                        min_index = min(tmp_list)
                        position_array[x, y, 0] = position_array[x+1, y, 0] = min_index
                if (y+1 <= shape[1]-1):
                    tmp_list = []
                    if (position_array[x, y+1, 0] != 0):
                        tmp_list.append(position_array[x, y, 0])
                        tmp_list.append(position_array[x, y+1, 0])
                        min_index = min(tmp_list)
                        position_array[x, y, 0] = position_array[x, y+1, 0] = min_index
    
    for y in range(0, shape[1]):
        for x in range(0, shape[0]):
            if (position_array[x, y, 0] != 0):
                tmp_list = []
                if (y-1 >= 0):
                    if (position_array[x, y-1, 0] != 0):
                        tmp_list.append(position_array[x, y, 0])
                        tmp_list.append(position_array[x, y-1, 0])
                        min_index = min(tmp_list)
                        position_array[x, y, 0] = position_array[x, y-1, 0] = min_index
                if (x-1 >= 0):
                    tmp_list = []
                    if (position_array[x-1, y, 0] != 0):
                        tmp_list.append(position_array[x, y, 0])
                        tmp_list.append(position_array[x-1, y, 0])
                        min_index = min(tmp_list)
                        position_array[x, y, 0] = position_array[x-1, y, 0] = min_index
    

    for x in range(0, shape[0]):
        for y in range(0, shape[1]):
            if (position_array[x, y, 0] != 0):
                tmp_list = []
                if (x-1 >= 0):
                    if (position_array[x-1, y, 0] != 0):
                        tmp_list.append(position_array[x, y, 0])
                        tmp_list.append(position_array[x-1, y, 0])
                        min_index = min(tmp_list)
                        position_array[x, y, 0] = position_array[x-1, y, 0] = min_index
                if (y-1 >= 0):
                    tmp_list = []
                    if (position_array[x, y-1, 0] != 0):
                        tmp_list.append(position_array[x, y, 0])
                        tmp_list.append(position_array[x, y-1, 0])
                        min_index = min(tmp_list)
                        position_array[x, y, 0] = position_array[x, y-1, 0] = min_index
    total_list = []
    count_list = []
    for y in range(0, shape[1]):
        for x in range(0, shape[0]):
            
            if (position_array[x, y, 0] != 0):
                tmp_index = position_array[x, y, 0]
                if (tmp_index not in total_list):
                    total_list.append(tmp_index)
                    count_list.append(1)
                else:
                    list_index = total_list.index(tmp_index)
                    count_list[list_index] += 1
    #print ("total list: ", total_list)
    #print ("count list: ", count_list)
    ##### test
    for i in range(0, len(total_list)):
        if (count_list[i] <= 1):
            for x in range(0, shape[0]):
                for y in range(0, shape[1]):
                    if (position_array[x, y, 0] == total_list[i]):
                        tmp_list = []
                        tmp_list.append(position_array[x+1, y, 0])
                        tmp_list.append(position_array[x, y+1, 0])
                        min_index = min(tmp_list)
                        if (min_index == 0):
                            tmp_list.remove(0)
                            min_index = min(tmp_list)
                        position_array[x, y, 0] = min_index
    ##### test


    total_list = []
    for x in range(0, shape[0]):
        for y in range(0, shape[1]):
            tmp_index = position_array[x, y, 0]
            if (tmp_index not in total_list):
                total_list.append(tmp_index)
    total_list.remove(0)
    print ("total list: ", total_list)             
    print ("len of total list: ", len(total_list))
    count = 0
    total_img = np.zeros((shape))
    for x in range(0, shape[0]):
            for y in range(0, shape[1]):
                for j in range(0, 3):
                    total_img[x, y, j] = 255
    for i in range(0, len(total_list)):
        new_img = np.zeros((shape))
        for x in range(0, shape[0]):
            for y in range(0, shape[1]):
                if (position_array[x, y, 0] == total_list[i]):
                    new_img[x, y, 2] = 255
                    total_img[x, y, 0] = total_img[x, y, 1] = total_img[x, y, 2] = int(count)*5
                    #print ("pixel: ", int(count)*5)
                #else:
                #    total_img[x, y, 0] = total_img[x, y, 1] = total_img[x, y, 2] = 255
        savename = "./words/" + str(count) + ".png"
        cv2.imwrite(savename, new_img)
        count += 1
    savename = "total.png"
    cv2.imwrite(savename, total_img)


def sortwords():
    sort_list = []
    for filename in os.listdir("./words/"):
        print (filename)
        name = "./words/" + filename
        #print (name)
        tmp_total = []
        tmp_list = []
        tmp_x = []
        tmp_y = []
        img = cv2.imread(name)
        shape = img.shape
        
        for x in range(0, shape[0]):
            for y in range(0, shape[1]):
                if (img[x, y, 2] == 255):
                    total_pix = int(x) + int(y)
                    tmp_list.append(total_pix)
                    tmp_x.append(x)
                    tmp_y.append(y)
        #print ("tmp list: ", tmp_list)
        min_total = min(tmp_list)
        min_index = tmp_list.index(min_total)
        min_x = tmp_x[min_index]
        min_y = tmp_y[min_index]
        print (min_total, min_x, min_y)
        
        tmp_total.append(min_total)
        tmp_total.append(min_x)
        tmp_total.append(min_y)
        sort_list.append(tmp_total)        
    
        
    print ("sort list: ", sort_list)


        #tmp_sort = min(tmp_list)
    #pass
                

if __name__ == "__main__":
    singlewords()
    sortwords()
                