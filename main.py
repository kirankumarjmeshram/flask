from flask import Flask
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv

load_dotenv()

mongoURI = os.getenv("URI")
app = Flask(__name__)
app.config["MONGO_URI"] = mongoURI
mongo = PyMongo(app)


@app.route("/")
def hello_world():
    mongo.db.flaskdb.insert_one({"b":"Hello World"})
    return "<p>Hello, World!</p>"

app.run(debug=True, port=5001)