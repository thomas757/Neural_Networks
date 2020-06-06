#!/usr/bin/python3

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

#define sequential model with 2 layers
model = keras.Sequential()
model.add(keras.Input(shape=(50,1)))
model.add(layers.Dense(2, activation="relu"))
model.add(layers.Dense(3, activation="relu"))

#Call model on a test input (not a drum)
#x = tf.ones((3, 3))
#y =model(x)

model.summary()
