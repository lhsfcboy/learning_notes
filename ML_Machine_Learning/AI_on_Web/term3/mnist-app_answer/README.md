# MNIST Flask App

## 概要
このプログラムは、FlaskとKerasを用いた、AI Webアプリを実装したプログラムになります
アプリとして、手書き文字認識を行うWebアプリを実装していきます

## フォルダ・プログラム概要
フォルダとの構成とプログラムの概要は以下となっております

- model
  - train.py
    - 手書き文字認識のモデルを学習し、モデルを保存します
- static
  - Webアプリで入力された画像データが保存されます
- templates
  - index.html 
    - Webアプリの画面を構成するHTMLです
- app.py
    - FalskによるWebサーバーを立ち上げるプログラムです
- README.md
  - 本プログラムの概要を記述しています
- requirements.txt
  - 必要なライブラリが列挙されているファイルです


## Cloud9における環境構築
```
# git環境とpyhton環境の構築
sudo yum install git

git clone https://github.com/yyuu/pyenv.git ~/.pyenv
git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
echo 'export PYENV_ROOT=$HOME/.pyenv
export PATH=$PYENV_ROOT/bin:$PATH
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile

source ~/.bash_profile
pyenv install 3.6.2
pyenv global 3.6.2

# 必要ライブラリのinstall
# requirements.txtに書かれたライブラリをinstallします
pip install --upgrade -r requirements.txt
```


## モデルの学習
学習モデルを構築するコマンドは、以下となっています
```
cd model
python3 train.py
```


## デプロイ
Webアプリの立ち上げコマンドは以下となっています
```
python3 app.py
```
