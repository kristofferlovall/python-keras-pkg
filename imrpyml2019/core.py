# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os, pkg_resources

import tensorflow as tf
from tensorflow import keras

import numpy as np
from tensorflow.keras.preprocessing import image

def getClassNames():
    # Class names
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    return class_names

def classify(fileInput):

    print("Trying to classify: " + fileInput)
    
    # Load model
    modelfile = 'my_model.h5'
    modelpath = pkg_resources.resource_filename(__name__, modelfile)
    new_model = keras.models.load_model(modelpath)

    # Load images
    img_width, img_height = 28, 28

    img = image.load_img(fileInput, target_size=(img_width, img_height))
    x = np.asarray(img)
    x = x[:,:,0]
    x = 255 - x
    x = x/255.
    x = np.expand_dims(x, axis=0)

    # Predict image
    prediction = new_model.predict(x)
    result = np.argmax(prediction[0])

    # Print out information
    class_names = getClassNames()

    print("Image " + fileInput + " is classified as " + class_names[result])

    return 0
