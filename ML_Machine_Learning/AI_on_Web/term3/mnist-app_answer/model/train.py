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
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# reshape関数を用いて、（データ数, 28, 28, 1）の形に変形させてください
X_train = X_train.reshape(60000, 28, 28, 1)
X_test = X_test.reshape(10000, 28, 28, 1)

# X_train, X_testをfloat32にキャストしてください
# 画素値を255で割ることによって、画像の正規化を行なってください
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

X_train = X_train[:12000]
y_train = y_train[:12000]
X_test = X_test[:2000]
y_test = y_test[:2000]

# y_train, y_testをカテゴリカル変数へ変換して下さい
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)


# CNNモデルを構築してください
model = Sequential()
model.add(Conv2D(32, (3, 3), padding='same', input_shape=X_train.shape[1:]))
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(10))
model.add(Activation('softmax'))

# モデルをコンパイルしてください
model.compile(
    loss='categorical_crossentropy',
    optimizer=Adam(),
    metrics=['accuracy']
)


# 学習を実行して下さい
# Write Me
history = model.fit(
    X_train,
    y_train,
    batch_size=batch_size,
    epochs=epochs,
    verbose=1,
    validation_data=(X_test, y_test)
)

# テストスコアの計算・表示をしてください
score = model.evaluate(X_test, y_test, verbose=1)
print('test loss:', score[0])
print('test acc:', score[1])


# model.saveによって、モデルを保存してください
# ファイル名は、model.h5とします
model.save('model.h5')
