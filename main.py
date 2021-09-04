from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        print(username)
        return render_template('home.html', username=username)

@app.route('/login/<username>', methods=['GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')


# if __name__ == "__main__":
#     app.run(debug=True)