import tensorflow as tf
from tensorflow.keras.layers import Layer
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
import pickle
import time
import pandas as pd

# make this exportable

class L1Dist(Layer): 
    def __init__(self, **kwargs): 
        super().__init__() # inheritance of base methods

    def call(self, input_emb, validation_emb): 
        return tf.math.abs(input_emb - validation_emb) # similirity comparison
    
    

def preprocess_image(path): 
    """
    
    This function takes in a path to an image and returns a tensor of the image

    Parameters
    ----------
    path : str
        path to the image

    Returns
    -------
    img : tensor
    """

    bimg = tf.io.read_file(path) # read the file
    img = tf.image.decode_jpeg(bimg) # decode the image
    img = tf.image.resize(img, (100,100)) # resize the image
    img = img/255.0 # normalize the image
    return img



