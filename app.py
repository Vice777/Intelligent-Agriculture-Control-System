
# Import flask and datetime module for showing date and time
import pickle

import numpy
import numpy as np
from flask import Flask
from flask import request
import datetime
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import cv2
from new import quality
import os
from wheat_disease_2 import show

# Initializing flask app
app = Flask(__name__)
cors=CORS(app)

x = datetime.datetime.now()
UPLOAD_FOLDER = "C:/Users/Asus/Desktop/New folder/image/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['CORS_HEADERS'] = 'Content-Type'

# Route for seeing a data
@app.route('/soil', methods = ['GET','POST'])
def get_image():
    if 'image' not in request.files:
        return "No image found"
    # read image file string data
    file = request.files['image']
    path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)
    # filename = secure_filename(file.filename)
    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    res = quality(path)
    return res

@app.route('/disease', methods = ['GET','POST'])
def get_disease():
    if 'image' not in request.files:
        return "No image found"
    # read image file string data
    file = request.files['image']
    path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)
    # filename = secure_filename(file.filename)
    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    res = quality(path)
    return res

@app.route('/wheatDisease', methods = ['GET','POST'])
def wheat_disease():
    if 'image' not in request.files:
        return "No image found"
    # read image file string data
    file = request.files['image']
    path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)
    # filename = secure_filename(file.filename)
    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    res = show(path)
    return res

@app.route('/', methods = ['GET'])
def hello():
    print("HELLO!")
    return "Yo!"

# Running app
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3001)