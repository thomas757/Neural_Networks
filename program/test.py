# Based on: https://machinelearningmastery.com/how-to-develop-multilayer-perceptron-models-for-time-series-forecasting/

# univariate data preparation
import numpy as np
from numpy import array
# from keras.models import Sequential
# from keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import os

# 16 for short test sample, 200 for big_test
length_train = 200

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

# define input sequence (choose 1)
## Very basic input
# raw_seq = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
## Little bit less completely basic input
# raw_seq = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
## Combination of the two
# raw_seq = [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]

#### This doesnt work yet: (I was trying to read from a file)
# raw_seq = []

# with open('input.txt') as input:
# 	raw_seq = input.read().splitlines()
# 	# raw_seq.append(input.readlines())

# for i in raw_seq:
# 	print("rawseq = ", i)
# 	i = int(i)
# 	print("deze is int yes no: ", isinstance(i, int))
# print("rawseq: ", raw_seq)

### Trying to read from a file...again :)
raw_seq = np.loadtxt("big_test.txt", dtype=int).tolist()

######This works again:

# choose a number of time steps
n_steps = length_train
# split into samples
X, y = split_sequence(raw_seq, n_steps)
# summarize the data
# for i in range(len(X)):
# 	print(X[i], y[i])

# initialize output thing
output = []

# define model
model = Sequential()
model.add(Dense(100, activation='relu', input_dim=n_steps))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])
# fit model
model.fit(X, y, epochs=12, verbose=2)
size = len(raw_seq) - length_train
maximum = 120
i = 0
# demonstrate prediction
while i < size and size < maximum:
    # print("rawseq = ", raw_seq)
    x_input = array(raw_seq[i:(i + length_train)])
    # print("x_input is first: ", x_input)
    x_input = x_input.reshape((1, n_steps))
    # print("x_input is then: ", x_input)
    yhat = model.predict(x_input, verbose=0)
    # print(int(yhat))
    raw_seq.append(int(yhat))
    output.append(int(yhat))
    size += 1
    # print("size in ", i, "is now: ", size)
    i += 1

print("raw: ", raw_seq)
print("output: ", output)

dir_path = os.path.dirname(os.path.realpath(__file__))
save_path = os.path.join(dir_path, "network_model")

if not os.path.exists(save_path):
    os.mkdir(save_path)

model.save(os.path.join(save_path, "model_classifier.h5"))
model = None
print("Done")
