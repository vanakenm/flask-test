from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/profile')
def show_user_profile():
    # show the user profile for that user
    return render_template('profile.html', username=request.args.get('name', ''))

