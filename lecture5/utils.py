#-*- coding: utf-8 -*-

import itertools
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image

IMG_SHAPE = (28, 28)
IMG_CHANNELS = 1

def to_categorical(y, num_classes=None):
  """Converts a class vector (integers) to binary class matrix.
  E.g. for use with categorical_crossentropy.
  # Arguments
    y: class vector to be converted into a matrix
      (integers from 0 to num_classes).
    num_classes: total number of classes.
  # Returns
    A binary matrix representation of the input.
  """
  y = np.array(y, dtype='int').ravel()
  if not num_classes:
    num_classes = np.max(y) + 1
  n = y.shape[0]
  categorical = np.zeros((n, num_classes))
  categorical[np.arange(n), y] = 1
  return categorical

def calculate_accuracy(y_target, y_pred):
  """Returns accuracy
  # Arguments
    y_target: true label data
    y_pred: estimated label data
  # Returns
    accuracy
  """

  return y_target[y_target == y_pred].size * 1.0 / y_target.size

def plot_confusion_matrix(cm, classes,
                          cmap=plt.cm.Blues):
  """This function prints and plots the confusion matrix.
  # Arguments
    cm: confusion matrix
    classes: lists of class names
    cmap: color map
  # Returns
    None
  """
  plt.imshow(cm, interpolation='nearest', cmap=cmap)
  plt.colorbar()
  tick_marks = np.arange(len(classes))
  plt.xticks(tick_marks, classes)
  plt.yticks(tick_marks, classes)

  thresh = cm.max() / 2.
  for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
    plt.text(j, i, cm[i, j],
             horizontalalignment="center",
             verticalalignment="center",
             size=10,
             color="white" if cm[i, j] > thresh else "black")

  plt.tight_layout()
  plt.ylabel('True label')
  plt.xlabel('Predicted label')

def get_image_array(X, index, shp=IMG_SHAPE, channels=IMG_CHANNELS):
  """Get one image array with dtype=uint8 from the list of images with dtype=float.
  # Arguments
    X: array like. The first dimension corresponds to the number of data,
      and the rest corresponds image shape.
    index: integer which specifies the data index you want.
    shp: image shape
    channels: number of image channels
  # Returns
    array like
  """
  ret = (X[index] * 255.).reshape(channels, shp[0], shp[1]) \
        .transpose(1,2,0).clip(0,255).astype(np.uint8)
  if channels == 1:
    ret = ret.reshape(shp[0], shp[1])
  return ret

def get_image_tile(data, width, height, shp=IMG_SHAPE, channels=IMG_CHANNELS):
  """Get PIL.Image object with a series of images.
  # Arguments
    data: array like. The first dimension corresponds to the number of data,
      and the rest corresponds image shape.
    width: tile width
    height: tile height
    shp: image shape
    channels: number of image channels
  # Returns
    PIL.Image object
  """
  if channels == 1:
    mode = 'L'
  elif channels == 3:
    mode = 'RGB'
  elif channels == 4:
    mode = 'RGBA'
  else:
    raise TypeError('arg channles must be 1, 3, or 4 (each number corresponds to image mode: \'L\', \'RGB\', and \'RGBA\')')

  im = Image.new(mode, (shp[0]*width, shp[1]*height))
  for (x, y), val in np.ndenumerate(np.zeros((width, height))):
    im.paste(
      Image.fromarray(
        get_image_array(
          data,
          x+y*width
        )
      ),
      (x*shp[0], y*shp[1])
    )
  return im
