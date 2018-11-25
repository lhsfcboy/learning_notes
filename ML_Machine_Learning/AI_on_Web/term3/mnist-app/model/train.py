import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD, Adam
from keras.layers import Conv2D, MaxPooling2D, Flatten
from keras.datasets import mnist

# バッチサイズ
batch_size = 128
# エポック数
epochs = 5

# mnistデータをロードしてください



# reshape関数を用いて、（データ数, 28, 28, 1）の形に変形させてください
# Write Me



# X_train, X_testをfloat32にキャストしてください
# 画素値を255で割ることによって、画像の正規化を行なってください
# Write Me


# y_train, y_testをカテゴリカル変数へ変換して下さい
# Write Me


# CNNモデルを構築してください
# Write Me


# モデルをコンパイルしてください
# Write Me



# 学習を実行して下さい
# Write Me

# テストスコアの計算・表示をしてください
# Write Me


# model.saveによって、モデルを保存してください
# ファイル名は、model.h5とします
# Write Me

