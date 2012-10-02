#!/usr/bin/python
# -*- coding: utf8 -*- 
from flask import Flask
from flask import render_template

#define app
app = Flask(__name__) 

@app.route('/home/')
def home():
    return render_template("home.html")

@app.route('/nav/')
def nav():
    return render_template("navigation.html")

@app.route('/search/')
def search():
    return render_template("search.html")
    

if __name__ == "__main__":
    app.run()
