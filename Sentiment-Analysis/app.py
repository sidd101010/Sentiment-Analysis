#step:1  Load the all necessary Library
from flask import Flask,render_template,flash,request,url_for,redirect, session
import numpy as np
import pandas as pd
import re
import os
import tensorflow as tf
from numpy import array
from keras.datasets import imdb
from keras.preprocessing import sequence
from keras.models import load_model

#step:2  here we define the path of image
IMAGE_FOLDER = os.path.join('static', 'img_pool')

#step:3  We have create the Flask application instance
app = Flask(__name__)

#step:4  We have to define the where we store the uploaded file
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

#step:5 We have to initilize the function
def init():
    global model,graph
    # load the pre-trained Keras model
    model = load_model('sentiment_analysis.h5')
    graph = tf.get_default_graph()

#step:6 You have define the decoratore for which functionality you have to chose
#########################Code for Sentiment Analysis
@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template("home.html")




