from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/say_hello')
def say_hello():
    # show the user profile for that user
    return render_template('hello.html', name=request.args.get('name', ''))

