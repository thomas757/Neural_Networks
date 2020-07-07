#!/usr/bin/python3

import os
import numpy as np
from numpy import array
from tensorflow.keras.models import load_model
import sys

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

# get file names from arguments
load_file = sys.argv[1]
if (len(sys.argv) > 2):
    save_file = sys.argv[2]

# input testing data
raw_seq = np.loadtxt(load_file, dtype=int).tolist()

# the length of one song
length_train = 400

# choose a number of time steps
n_steps = length_train

# split into samples
X, y = split_sequence(raw_seq, n_steps)

# initialize output array
output = []

# initialize parameters for predicting
maximum = 400
i = 0

# determine the path of the network model
dir_path = os.path.dirname(os.path.realpath(__file__))
save_path = os.path.join(dir_path, "network_model")
model_path = os.path.join(save_path, "model_classifier.h5")

# load the network model
model = load_model(model_path)
model.predict(np.zeros((1, length_train)))

# demonstrate prediction
while i < maximum:
    x_input = array(raw_seq[i:(i + length_train)])
    x_input = x_input.reshape((1, n_steps))
    yhat = model.predict(x_input, verbose=0)
    raw_seq.append(int(yhat))
    output.append(int(yhat))
    i += 1

# prints the output
print("output: ", output)
print("length output: ", len(output))

# save the prediction
file = open(save_file, "w")
np.savetxt(file, output, fmt='%d')
file.close()