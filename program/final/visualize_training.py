# Based on: https://machinelearningmastery.com/how-to-develop-multilayer-perceptron-models-for-time-series-forecasting/
# Written by Isabelle Tilleman (s3656586)
from numpy import array
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.optimizers import Adam
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# split a univariate sequence into samples
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


# get file name from arguments
load_file = sys.argv[1]

# input training data
raw_seq = np.loadtxt(load_file, dtype=int).tolist()

# the length of one song
length_train = 32

# choose a number of time steps
n_steps = length_train

# split into samples
X, y = split_sequence(raw_seq, n_steps)

# define model
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=n_steps))
model.add(Dropout(0.1))
model.add(Dense(1))
model.summary()
opt = Adam(learning_rate=0.01)
model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

# fit model
history = model.fit(X, y, validation_split=0.33, epochs=12, verbose=2)
print(history.history.keys())

# summarize history for loss
plt.plot(history.history['loss'])
plt.title('Model loss during training')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.savefig('lossPlot4.png')
