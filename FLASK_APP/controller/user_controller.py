from app import app
@app.route("/user/signup")
def signup():
    return "This is Signup operation"