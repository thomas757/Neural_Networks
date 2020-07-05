#!/usr/bin/python3

import os
import numpy as np
import tensorflow as tf
from tensorflow import data

# dir_path = os.path.dirname(os.path.realpath(__file__))
# save_path = os.path.join(dir_path, "network_model")
# print(save_path)

# raw_seq = [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]

# print("input:", raw_seq)
# file = open("prediction.txt", "w")
# np.savetxt(file, raw_seq, fmt='%d')
# file.close()

# original_array = np.loadtxt("prediction.txt", dtype=int)
# print("output:", original_array)

dataset = tf.data.TextLineDataset(["prediction.txt", "test.txt"])

for element in dataset:
    print(element.numpy())
