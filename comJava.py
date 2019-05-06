# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:27:11 2019

@author: user
"""

import os

def com_java(filename, path):
    process = os.popen("javac "+filename+".java 2> err.txt")
    process.close()
    fsize = os.stat('C:/Users/user/Documents/000PSL/err.txt').st_size
    print(fsize)
    if fsize != 0:
        with open ("err.txt", "r") as myfile:
            data = myfile.read()
            print('Java err:', data)
    else:
        process = os.popen("java "+filename+".java > out.txt")
        process.close()
        with open ("out.txt", "r") as myfile:
            data = myfile.read()
            print('Java:', data)        
