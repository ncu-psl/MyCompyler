# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:24:20 2019

@author: user
"""

import os

def com_cpp(filename, path):
    process = os.popen("g++ -o "+filename+" "+filename+".cpp 2> err.txt")
    process.close()
    fsize = os.stat('C:/Users/user/Documents/000PSL/err.txt').st_size
    print(fsize)
    if fsize != 0:
        with open ("err.txt", "r") as myfile:
            data = myfile.read()
            print('C++ err:', data)
    else:
        process = os.popen(filename+".exe > out.txt")
        process.close()
        with open ("out.txt", "r") as myfile:
            data = myfile.read()
            print('C++:', data)