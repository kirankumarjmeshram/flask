from app import app
from flask import request
from flask import jsonify

from model.user_model import user_model # from model folder import class user_model from user_model.py file
obj = user_model()



@app.route("/user/signup")
def user_getall_controllerr():
    return obj.user_getall_model()


@app.route("/user/addone", methods = ["POST"])
def user_addone_controller():
    # print("con",request.form)
    user_data = request.form
    obj.user_addone_model(user_data)
    return "user added successfully"

# @app.route("/user/addone", methods=["POST"])
# def user_addone_controller():
#     try:
#         user_data = request.form
#         result = obj.user_addone_model(user_data)
        
#         if "Error" in result:
#             return jsonify({"message": "Error adding user", "error": result}), 500
#         else:
#             return jsonify({"message": "User added successfully"}), 201
#     except Exception as e:
#         return jsonify({"message": "Internal server error", "error": str(e)}), 500

@app.route("/user/update", methods = ["PUT"])
def user_update_controller():
    # print("con",request.form)
    user_data = request.form
    return obj.user_update_model(user_data)
    # return "user updated successfully"


@app.route("/user/delete/<id>", methods = ["DELETE"])
def user_delete_controller(id):
    return obj.user_delete_model(id)