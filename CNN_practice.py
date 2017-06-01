import cv2
import tensorflow as tf
import os
import numpy as np


sess = tf.InteractiveSession()

filenames = []
for root, dirs, files in os.walk():
	filenames = files