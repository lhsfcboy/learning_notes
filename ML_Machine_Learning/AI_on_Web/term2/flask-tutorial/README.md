# Flask Tutorial

## 概要
本プログラムは、FlaskによるWebアプリ作成のチュートリアルとなります
Flaskを用いたWebサーバーの立ち上げと、変数の渡し方など、基本的な扱いについて学習をします


## フォルダ・プログラム概要
フォルダとの構成とプログラムの概要は以下となっております
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


## デプロイ
Webアプリの立ち上げコマンドは以下となっています
```
python3 app.py
```
