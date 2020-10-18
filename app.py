from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hi there Daniel!'


@app.route('/about')
def about():
    return 'About page'
