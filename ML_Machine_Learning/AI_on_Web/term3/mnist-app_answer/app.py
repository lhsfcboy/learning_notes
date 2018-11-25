from flask import Flask, render_template, request
from scipy.misc import imsave, imread, imresize
import numpy as np
import keras.models
from keras.models import load_model
from datetime import datetime
import tensorflow as tf


app = Flask(__name__)
global model
# 変数modelに学習済みモデルをロードしてください
model = load_model("model/model.h5")

# Tensorflowによるグラフをセットします
graph = tf.get_default_graph()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # htmlをレンダリングするように命令します
        return render_template("index.html")

    if request.method == 'POST':
        # requestから、送られてきたファイルを取得します
        f = request.files['file']

        # 取得したファイルを、static以下に保存します
        filepath = "./static/" + datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
        f.save(filepath)

        # 保存されたファイルを読み込み、変数xにセットします
        x = imread(filepath, mode='L')

        # 学習データは、黒字に白文字のデータとなりますが、入力画像は今回の場合、白地に黒文字とするので、
        # np.invertを用いて、画素値を反転させます
        x = np.invert(x)

        # 画像を28x28のデータに変換をします
        # さらに、reshape関数を用いて、(1, 28, 28, 1)次元のデータに変換します
        x = imresize(x, (28, 28))
        x = x.reshape(1, 28, 28, 1)

        # データをfloat32に変換した後に、225で割ることによって、画像を正規化します
        x = x.astype('float32')
        x /= 255


        with graph.as_default():
            # 入力データxに対して、モデルを適用し、各ラベルの予測確率を取得します
            out = model.predict(x)

            # 最も予測確率の高いラベルを文字列型で取得します
            predict = str(np.argmax(out, axis=1)[0])

        # htmlをレンダリングするように命令します
        # 画像データのfilepathと、モデルによって、予測された結果をレンダリング先のhmtlに渡します
        return render_template('index.html', filepath=filepath, predict=predict)


if __name__ == '__main__':
    # Webアプリを起動します
    app.debug = True
    port = 5000
    app.run(host='0.0.0.0', port=port)
