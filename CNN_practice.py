import cv2
import tensorflow as tf
import os
import numpy as np


sess = tf.InteractiveSession()

def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)

def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                        strides=[1, 2, 2, 1], padding='SAME')

filenames = []

for root, dirs, files in os.walk('/Users/lordent/Desktop/train'):
	filenames = files
testpath = '/Users/lordent/Desktop/train/'

for i in range(0, len(filenames)):
	if filenames[i][:3] == 'dog':
		verification = 1
	else:
		verification = 0
	
	image = cv2.imread(testpath + filenames[i])
	height, width, dim = image.shape()

	if height < width:
		image = cv2.resize(image, (128, image.shape[0]*128//image.shape[1]))
	else:
		image = cv2.resize(image, (image.shape[0]*128//image.shape[1], 128))
	img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	#img_gray = cv2.blur(gray, (5, 5))