import requests
import json
import math
from flask import Flask,json, render_template, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import os
import getdata
app = Flask(__name__)
api = Api(app)
app.config['UPLOAD_FOLDER'] = 'static/files'



@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/results", methods = ['GET'])
def write():
    data = getdata.GetData()    
    return render_template('index.html',test = data)
    

if __name__ == '__main__':
    app.run()  

