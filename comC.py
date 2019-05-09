# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:25:35 2019

@author: user
"""

import os

def com_c(filename, path):
    os.chdir(path)
    process = os.popen("gcc -o "+filename+" "+filename+".c 2> out.txt")
    process.close()
    fsize = os.stat('C:/Users/user/Documents/000PSL/out.txt').st_size
    print(fsize)
    if fsize != 0:
        with open ("out.txt", "r") as myfile:
            data = myfile.read()
            print('C err:', data)
    else:
        process = os.popen(filename+".exe > out.txt")
        process.close()
        with open ("out.txt", "r") as myfile:
            data = myfile.read()
            print('C:', data)
            
if __name__== "__main__":
    com_c("hello", "C:/Users/user/Documents/000PSL")