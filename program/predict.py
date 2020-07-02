#!/usr/bin/python3

import os
import tensorflow
import numpy as np
from numpy import array
from tensorflow.keras.models import load_model


def split_sequence(sequence, n_steps):
    X, y = list(), list()
    for i in range(len(sequence)):
        # find the end of this pattern
        end_ix = i + n_steps
        # check if we are beyond the sequence
        if end_ix > len(sequence) - 1:
            break
        # gather input and output parts of the pattern
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return array(X), array(y)

raw_seq = [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0,
           1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
length_train = 16
n_steps = length_train
X, y = split_sequence(raw_seq, n_steps)
output = []
size = len(raw_seq) - length_train
maximum = 120
i = 0

dir_path = os.path.dirname(os.path.realpath(__file__))
save_path = os.path.join(dir_path, "network_model")
model_path = os.path.join(save_path, "model_classifier.h5")

model = load_model(model_path)
model.predict(np.zeros((1, length_train)))

while i < size and size < maximum:
    x_input = array(raw_seq[i:(i + length_train)])
    x_input = x_input.reshape((1, n_steps))
    yhat = model.predict(x_input, verbose=0)
    raw_seq.append(int(yhat))
    output.append(int(yhat))
    size += 1
    i += 1

print("raw: ", raw_seq)
print("output: ", output)
