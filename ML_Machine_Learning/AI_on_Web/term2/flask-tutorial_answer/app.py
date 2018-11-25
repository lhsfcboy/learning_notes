from flask import Flask, render_template, request

app = Flask(__name__)


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return "Hello World!"


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return render_template("index.html")

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return render_template("index.html", message="Pythonによる深層学習")


if __name__ == '__main__':
    app.debug = True
    port = 5000
    app.run(host='0.0.0.0', port=port)
