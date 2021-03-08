# ExamForNTU question3

import tensorflow as tf
import pandas as pd
import numpy as np

# Define a function to read file
def read_file(file):
    f = open(file, "r")
    res = []
    for line in f.readlines():
        line = line.replace("\n", "")
        data = line.split('\t')
        res.append(data)
    f.close()
    return res

# Read the data of train set
trainData = read_file("train_data.txt")
trainData = pd.DataFrame(trainData[1:], columns=trainData[0])
trainData = trainData.astype(float)

# Read the truth of train set
trainTruth = read_file("train_truth.txt")
trainTruth = pd.DataFrame(trainTruth[1:], columns=trainTruth[0])
trainTruth = trainTruth.astype(float)

# Read the data of test set
testData = read_file('test_data.txt')
testData = pd.DataFrame(testData[1:], columns=testData[0])
testData = testData.astype(float)

# Construction of neural network (4 hidden layers)
# 'activation' means activation function
# 'input_shape' means the shape of every layer
model = tf.keras.Sequential([tf.keras.layers.Dense(4, input_shape = (3,), activation = 'relu'),
                            tf.keras.layers.Dense(4, input_shape = (4,), activation = 'relu'),
                            tf.keras.layers.Dense(4, input_shape = (4,), activation = 'relu'),
                            tf.keras.layers.Dense(4, input_shape = (4,), activation = 'relu'),
                            tf.keras.layers.Dense(1)
                            ])

# Model compilation
# 'loss' means loss function
model.compile(optimizer = 'adam', loss = 'mse')

# Train the model
model.fit(trainData, trainTruth, epochs = 50)

# Predict by the testData
res = model.predict(testData)

# Print
f = open("test_predicted.txt", "w")
print("y", file=f)
for i in range(len(res)):
    print(res[i][0], file=f)
f.close()



