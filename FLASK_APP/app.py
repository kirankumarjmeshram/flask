from flask import Flask


app = Flask(__name__)

# import controller.user_controller
# import controller.product_controller

from controller import user_controller, product_controller, product_categories_controller
# from controller import *

@app.route("/")
def welcome():
    return "Hello World"

@app.route("/home")
def home():
    return "This is my home"

app.run(debug=True, port=5001)