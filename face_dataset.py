import os
from os import listdir
from PIL import Image as Img
from numpy import asarray
from numpy import expand_dims
from matplotlib import pyplot
from keras.models import load_model
import numpy as np
import tensorflow as tf

import pickle
import cv2

HaarCascade = cv2.CascadeClassifier(cv2.samples.findFile(cv2.data.haarcascades + '/static/haarcascade_frontalface_default.xml'))

MyFaceNet = load_model("/static/facenet_keras.h5")


