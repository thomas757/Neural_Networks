# univariate data preparation
from numpy import array
# from keras.models import Sequential
# from keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

length_train = 8

# split a univariate sequence into samples
def split_sequence(sequence, n_steps):
	X, y = list(), list()
	for i in range(len(sequence)):
		# find the end of this pattern
		end_ix = i + n_steps
		# check if we are beyond the sequence
		if end_ix > len(sequence)-1:
			break
		# gather input and output parts of the pattern
		seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
		X.append(seq_x)
		y.append(seq_y)
	return array(X), array(y)

# define input sequence
# raw_seq = [10, 20, 30, 40, 50, 60, 70, 80, 90]
raw_seq = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
# choose a number of time steps
n_steps = length_train
# split into samples
X, y = split_sequence(raw_seq, n_steps)
# summarize the data
for i in range(len(X)):
	print(X[i], y[i])


# define model
model = Sequential()
model.add(Dense(100, activation='relu', input_dim=n_steps))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')
# fit model
model.fit(X, y, epochs=2000, verbose=0)
size = len(raw_seq)-length_train
print("size now =", size)
maximum = 50
i = 0
# demonstrate prediction
while i<size and size < maximum:
	# print("rawseq = ", raw_seq)
	x_input = array(raw_seq[i:(i+length_train)])
	# print("x_input is first: ", x_input)
	x_input = x_input.reshape((1, n_steps))
	# print("x_input is then: ", x_input)
	yhat = model.predict(x_input, verbose=0)
	print(int(yhat))
	raw_seq.append(int(yhat))
	size += 1
	# print("size in ", i, "is now: ", size)
	i += 1
# x_input = array([0, 1, 0, 0])
# x_input = x_input.reshape((1, n_steps))
# yhat = model.predict(x_input, verbose=0)
# toprint = int(yhat)
# # print(yhat)
# print(toprint)
print(raw_seq)
