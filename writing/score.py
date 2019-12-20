#score.py

import numpy as np
import csv


with open("score.csv") as csvfile:
    rows = csv.reader(csvfile)


    for row in rows:
        print (row)
        print (type(row))
        print (len(row))

