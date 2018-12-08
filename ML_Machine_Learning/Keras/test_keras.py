#coding: utf-8
from keras.datasets import mnist
import matplotlib.pyplot as plt
# 加载数据
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# 展示下第一张图
plt.imshow(X_train[0], cmap=plt.get_cmap('PuBuGn_r'))
plt.show()