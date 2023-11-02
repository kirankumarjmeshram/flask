from flask import Flask

app = Flask(__name__)

import user_controller

@app.route("/")
def welcome():
    return "Hello World"

@app.route("/home")
def home():
    return "This is my home"