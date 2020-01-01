# offset.py
# offset_table
# z = 0.35
import numpy as np
import cv2


def offset():
    #shape = (11,11,1)
    #offset_table = np.zeros((shape))

    offset_table = np.array([[ 0.406, 0.406, 0.405, 0.404, 0.403, 0.403, 0.401, 0.4,   0.399, 0.397, 0.397,\
                    0.406, 0.406, 0.405, 0.404, 0.403, 0.402, 0.401, 0.398, 0.4,   0.398, 0.397,\
                    0.404, 0.405, 0.404, 0.402, 0.402, 0.4,   0.4,   0.4,   0.398, 0.398, 0.395,\
                    0.406, 0.404, 0.404, 0.403, 0.401, 0.4,   0.399, 0.401, 0.4,   0.399, 0.398,\
                    0.405, 0.404, 0.404, 0.403, 0.402, 0.4,   0.399, 0.401, 0.398, 0.399, 0.395,\
                    0.406, 0.405, 0.404, 0.403, 0.402, 0.401, 0.4,   0.402, 0.401, 0.399, 0.398,\
                    0.406, 0.404, 0.402, 0.403, 0.401, 0.401, 0.399, 0.401, 0.399, 0.399, 0.395,\
                    0.406, 0.405, 0.403, 0.402, 0.4,   0.399, 0.397, 0.401, 0.4,   0.399, 0.398,\
                    0.405, 0.405, 0.404, 0.402, 0.401, 0.4,   0.398, 0.401, 0.397, 0.399, 0.395,\
                    0.406, 0.405, 0.404, 0.402, 0.401, 0.401, 0.399, 0.401, 0.399, 0.398, 0.397,\
                    0.406, 0.406, 0.405, 0.403, 0.403, 0.401, 0.399, 0.399, 0.398, 0.397, 0.396]])
    #print ("offset table: ", offset_table)
    #print ("shape: ", offset_table.shape)
    #print ("len: ", offset_table.shape[1])
    table_len = (offset_table.shape[1])
    #print ("table len: ", table_len)
    #print ("table [1]: ", offset_table[0, 2])
    count = 0
    for i in range(0, table_len):
        count += offset_table[0, i]

    average_count = round(float(count / 121), 3)
    #print ("average: ", average_count)
    for i in range(0, table_len):
        offset_table[0, i] -= average_count

    #print ("new table: ", offset_table)

    new_table = np.reshape(offset_table, (11, 11, 1))
    #print ("new table: ", new_table)
    #print ("shape: ", new_table.shape)
    #print ("specific: ", (list(new_table[3, 4])[0]))
    return (new_table)

def offset_test(offset_table):
    # (0.7, 0.2)-----------(0.9, 0.2)
    #          |           |
    #          |           |
    #          |           |
    # (0.7, -0.3)----------(0.9, -0.3)
    #print ("table shape: ", offset_table.shape)
    #print ("z tmp: ", round(offset_table[10,10][0], 3))
    origin_x = 0.7
    origin_y = 0.2
    origin_z = 0.25
    count = 0
    for i in range(0, 11):
        for j in range(0, 11):
            y = round(origin_y - (i * 0.05), 3)
            x = round(origin_x + (j * 0.02), 3)
            offset_z = round(offset_table[i, j][0], 3)
            z = round((origin_z - offset_z), 3)
            print (x, y, z)
            count += 1
    #print ("total count: ", count)

if __name__ == "__main__":
    offset_table = offset()
    offset_test(offset_table)