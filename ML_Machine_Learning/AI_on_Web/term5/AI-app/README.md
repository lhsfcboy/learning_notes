# MNIST Flask App

## 概要
このプログラムは、AI Webアプリケーション作成用のテンプレートとなっています。
独自で画像データを用意し、モデルを学習することによって、AI Webアプリケーションを作成してください。


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
# 必要な追加ライブラリがある場合は、requirementsにライブラリ名を追加してください
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
