import cv2 
import numpy as np

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
    

    for y in range(0, shape[1]):
        for x in range(0, shape[0]):
            if (position_array[x, y, 0] != 0):
                tmp_list = []
                if (y+1 < shape[1]-1):
                    if (position_array[x, y+1, 0] != 0):
                        tmp_list.append(position_array[x, y, 0])
                        tmp_list.append(position_array[x, y+1, 0])
                        min_index = min(tmp_list)
                        position_array[x, y, 0] = position_array[x, y+1, 0] = min_index
                if (x+1 < shape[0]-1):
                    tmp_list = []
                    if (position_array[x+1, y, 0] != 0):
                        tmp_list.append(position_array[x, y, 0])
                        tmp_list.append(position_array[x+1, y, 0])
                        min_index = min(tmp_list)
                        position_array[x, y, 0] = position_array[x+1, y, 0] = min_index
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
                    print ("pixel: ", int(count)*5)
                #else:
                #    total_img[x, y, 0] = total_img[x, y, 1] = total_img[x, y, 2] = 255
        savename = "./words/" + str(count) + ".png"
        cv2.imwrite(savename, new_img)
        count += 1
    savename = "total.png"
    cv2.imwrite(savename, total_img)

                

if __name__ == "__main__":
    singlewords()
                