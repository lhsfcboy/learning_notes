#coding: utf-8
#Simple CNN
import numpy
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils

seed = 7
numpy.random.seed(seed)

#加载数据
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# reshape to be [samples][channels][width][height]
X_train = X_train.reshape(X_train.shape[0],28, 28,1).astype('float32')
X_test = X_test.reshape(X_test.shape[0],28, 28,1).astype('float32')

# normalize inputs from 0-255 to 0-1
X_train = X_train / 255
X_test = X_test / 255

# one hot encode outputs
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]

# 简单的CNN模型
def baseline_model():
    # create model
    model = Sequential()
    #卷积层
    model.add(Conv2D(32, (3, 3), padding='valid', input_shape=(28, 28,1), activation='relu'))
    #池化层
    model.add(MaxPooling2D(pool_size=(2, 2)))
    #卷积
    model.add(Conv2D(15, (3, 3), padding='valid' ,activation='relu'))
    #池化
    model.add(MaxPooling2D(pool_size=(2, 2)))
    #全连接，然后输出
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# build the model
model = baseline_model()

# Fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=128, verbose=2)