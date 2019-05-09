# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 11:31:37 2019

@author: user
"""

import os

filename = 'hello'
# python
#os.popen("cd C:\\Users\\user\\Documents\\000PSL")

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
    
# c
process = os.popen("gcc -o "+filename+" "+filename+".c 2> err.txt")
process.close()
fsize = os.stat('C:/Users/user/Documents/000PSL/err.txt').st_size
print(fsize)
if fsize != 0:
    with open ("err.txt", "r") as myfile:
        data = myfile.read()
        print('C err:', data)
else:
    process = os.popen(filename+".exe > out.txt")
    process.close()
    with open ("out.txt", "r") as myfile:
        data = myfile.read()
        print('C:', data)
    
# cpp
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
        
# java
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
