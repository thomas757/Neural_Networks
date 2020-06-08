# https://pypi.org/project/perceptron/
# from perceptron import mlp

# def main():
# 	n = mlp.Net()

# 	for i in range(30):
# 		n.train([101,103],[201,202,203],201)
# 		n.train([102,103],[201,202,203],202)
# 		n.train([101],[201,202,203],203)
	
# 	print(n.eval([101,103,],[201,202,203]))
# 	print(n.eval([102,103],[201,202,203]))
# 	print(n.eval([103],[201,202,203]))

# if  __name__=='__main__': main()



# ---------------------------------------------------------------------------------------------------------------


# https://chrisalbon.com/machine_learning/basics/perceptron_in_scikit-learn/
# # Load required libraries
# from sklearn import datasets
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import Perceptron
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import numpy as np

# # Load the iris dataset
# iris = datasets.load_iris()

# # Create our X and y data
# X = iris.data
# y = iris.target

# # View the first five observations of our y data
# y[:5]
# # View the first five observations of our x data.
# # Notice that there are four independent variables (features)
# X[:5]

# # Split the data into 70% training data and 30% test data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# # Train the scaler, which standarizes all the features to have mean=0 and unit variance
# sc = StandardScaler()
# sc.fit(X_train)

# # Apply the scaler to the X training data
# X_train_std = sc.transform(X_train)

# # Apply the SAME scaler to the X test data
# X_test_std = sc.transform(X_test)

# # Create a perceptron object with the parameters: 40 iterations (epochs) over the data, and a learning rate of 0.1
# ppn = Perceptron(n_iter=40, eta0=0.1, random_state=0)

# # Train the perceptron
# ppn.fit(X_train_std, y_train)

# # Apply the trained perceptron on the X data to make predicts for the y test data
# y_pred = ppn.predict(X_test_std)

# # View the accuracy of the model, which is: 1 - (observations predicted wrong / total observations)
# print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))



# ---------------------------------------------------------------------------------------------------------------


# #!/usr/bin/python3

# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers
# from tensorflow.keras import losses

# x_train=[0,0,0,1,0,0,0,1,0,0,0,1]
# y_train=[0,0,0,1,0,0,0,1,0,0,0,1]
# x_test=[0,0,0,1]
# y_test=[0,0,0,1]

# #define sequential model with 2 layers
# #model = keras.Sequential()
# #model.add(keras.Input(shape=(12,1)))
# #model.add(layers.Dense(2, activation="relu"))
# #model.add(layers.Dense(3, activation="relu"))

# model = tf.keras.models.Sequential([
#   #tf.keras.layers.Flatten(input_shape=(28, 28)),
#   tf.keras.Input(1,1),
#   tf.keras.layers.Dense(12, activation='relu'),
#   tf.keras.layers.Dense(12, activation='relu')
# ])

# #Call model on a test input (not a drum)
# #x = tf.ones((3, 3))
# #y =model(x)

# loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])
# model.fit(x_train,y_train, epochs=12, batch_size=1)

# model.summary()

# model.evaluate()
# model.predict()



# ---------------------------------------------------------------------------------------------------------------



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





# https://github.com/Fodark/mlp-python
# https://towardsdatascience.com/implementing-a-multi-layer-perceptron-neural-network-in-python-b22b5a3bdfa3