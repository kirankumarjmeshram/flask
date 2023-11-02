from flask import Flask

app = Flask(__name__)

# import controller.user_controller
# import controller.product_controller

from controller import user_controller, product_controller

@app.route("/")
def welcome():
    return "Hello World"

@app.route("/home")
def home():
    return "This is my home"