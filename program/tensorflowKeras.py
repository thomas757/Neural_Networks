#!/usr/bin/python3

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import losses

x_train=[0,0,0,1,0,0,0,1,0,0,0,1]
y_train=[0,0,0,1,0,0,0,1,0,0,0,1]
x_test=[0,0,0,1]
y_test=[0,0,0,1]

#define sequential model with 2 layers
#model = keras.Sequential()
#model.add(keras.Input(shape=(12,1)))
#model.add(layers.Dense(2, activation="relu"))
#model.add(layers.Dense(3, activation="relu"))

model = tf.keras.models.Sequential([
  #tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.Input(1,1),
  tf.keras.layers.Dense(12, activation='relu'),
  tf.keras.layers.Dense(12, activation='relu')
])

#Call model on a test input (not a drum)
#x = tf.ones((3, 3))
#y =model(x)

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])
model.fit(x_train,y_train, epochs=12, batch_size=1)

model.summary()

model.evaluate()
model.predict()
