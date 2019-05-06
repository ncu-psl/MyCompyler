# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:20:38 2019

@author: user
"""
import os

def com_py(filename, path):
    os.chdir("C:/Users/user/Documents/000PSL")
    process = os.popen("python "+filename+".py > out.txt")
    process.close()
    fsize = os.stat('C:/Users/user/Documents/000PSL/out.txt').st_size
    print(fsize)
    if fsize == 0:
        process = os.popen("python "+filename+".py 2> err.txt")
        process.close()
        with open ("err.txt", "r") as myfile:
            data = myfile.read()
            print('Py err:', data)
    else:
        with open ("outp.txt", "r") as myfile:
            data = myfile.read()
            print('Py:', data) 