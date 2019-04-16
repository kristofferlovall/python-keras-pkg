# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os, pkg_resources

import tensorflow as tf
from tensorflow import keras

import numpy as np
from tensorflow.keras.preprocessing import image

# For reproducibility
from numpy.random import seed
from tensorflow import set_random_seed

def getClassNames():
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    return class_names

def classify(fileInput):

    seed(1)
    set_random_seed(2)

    print("Trying to classify: " + fileInput)
    
    # Load pre-generated model
    modelfile = 'my_model.h5'
    modelpath = pkg_resources.resource_filename(__name__, modelfile)
    new_model = keras.models.load_model(modelpath)

    # Image dimensions
    img_width, img_height = 28, 28

    # Load image with a specified dimension
    img = image.load_img(fileInput, target_size=(img_width, img_height))

    # Convert to numpy array
    x = np.asarray(img)

    # Get only one channel
    x = x[:,:,0]

    # Inverse value
    x = 255 - x

    # We use 0 - 1 range
    x = x/255.

    # Put it inside an array of image
    x = np.expand_dims(x, axis=0)

    # Predict image
    prediction = new_model.predict(x)
    result = np.argmax(prediction[0])

    # Print out information
    class_names = getClassNames()
    print("Image " + fileInput + " is classified as " + class_names[result])

    return result
