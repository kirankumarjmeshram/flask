import mysql.connector
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

import json

class user_model():
    def __init__(self):
        #connection establishment code
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password=os.environ.get("PASS"), database="flask_tutorial")
            self.con.autocommit = True
            #cursor helps for DML ops
            self.cur = self.con.cursor(dictionary=True)
            print("Connection successful")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def user_getall_model(self):
        #query execution code
        try:
            self.cur.execute("SELECT * FROM user")
            result = self.cur.fetchall()
            if len(result) > 0:
                return json.dumps(result)
            else:
                return "No data found"
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return "An error occurred while fetching data."

    def user_addone_model(self, data):
        try:
            self.cur.execute(f"INSERT INTO user(name, email, phone, role, password) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
            return "User created successfully"
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return "An error occurred while creating the user."

# Example usage
model = user_model()
