from app import app
@app.route("/product/add")
def add_product():
    return "This is add to cart operation"