# crawl_color.py

#! /usr/bin/env python
import cv2
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

from bs4 import BeautifulSoup
import pandas as pd


def color_table():
    url = 'https://www.ebaomonthly.com/window/photo/lesson/colorList.htm'
    color_table = pd.read_html(url)[1]
    useful_table = color_table[['R', 'G', 'B']]
    #print ("useful info: ", useful_table)
    np_table = useful_table.to_numpy()
    #print (type(np_table))
    #print (np_table)
    #print (np_table.shape)
    cv2.imwrite("color_table.png", np_table)
    return (np_table)

if __name__ == "__main__":
    np_table = color_table()
    print (np_table)
