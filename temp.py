# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
import comPy, comCpp, comC, comJava
app = Flask(__name__)

@app.route("/")

def index():
         return render_template("index.html")

def outputTXT():
    if lang == 1:
        return comC.com_c(filename, path)
    elif lang == 2:
        return comCpp.com_cpp(filename, path)
    elif lang == 3:
        return comPy.com_py(filename, path)
    elif lang == 4:
        return comJava.com_java(filename,path)
    
if __name__ == '__main__':
        app.run(host="127.0.0.1", port="5000", debug=True)
    