from flask import Flask, render_template, request
from scipy.misc import imsave, imread, imresize
import numpy as np
import keras.models
from keras.models import load_model
from datetime import datetime
import tensorflow as tf


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':        
        return render_template("index.html")

    # if request.method == 'POST':
    #     return render_template('index.html')


if __name__ == '__main__':
    # Webアプリを起動します
    app.debug = True
    port = 5000
    app.run(host='0.0.0.0', port=port)
