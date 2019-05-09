# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:20:38 2019

@author: user
"""

import os

def com_py(filename, path):
    os.chdir(path)
    process = os.popen("python "+filename+".py > out.txt")
    process.close()
    fsize = os.stat(path + '/out.txt').st_size
    print(fsize)
    if fsize == 0:
        process = os.popen("python "+filename+".py 2> out.txt")
        process.close()
        with open ("out.txt", "r") as myfile:
            data = myfile.read()
            print('Py err:', data)
    else:
        with open ("out.txt", "r") as myfile:
            data = myfile.read()
            print('Py:', data)
            
if __name__== "__main__":
    com_py("myCode", "C:/Users/user/Downloads")