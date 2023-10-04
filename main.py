from flask import Flask
from flask_pymongo import PyMongo

mongoURI = ""
app = Flask(__name__)
app.config["MONGO_URI"] = mongoURI
mongo = PyMongo(app)


@app.route("/")
def hello_world():
    mongo.db.flaskdb.insert_one({"a":"Hello WOrld"})
    return "<p>Hello, World!</p>"

app.run(debug=True, port=5001)