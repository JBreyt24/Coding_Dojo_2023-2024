
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


class User:
    db = "flaskoctohana"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @staticmethod
    def validate_user(request):
        is_valid = True
        print(len(request['age']))
        if len(request["first_name"]) < 1:
            is_valid = False
            flash("Please provide first name", "reg")
        elif len(request["last_name"]) < 1:
            is_valid = False
            flash("Please provide last name", "reg")
        if len(request["age"]) < 1:
            is_valid = False
            flash("Please provide age", "reg")
        elif int(request["age"]) <18:
            is_valid = False
            flash("Must be older than 18 years of age", "reg")
        if len(request["email"]) < 1:
            is_valid = False
            flash("Please provide email", "reg")
        elif not EMAIL_REGEX.match(request["email"]):
            flash("Invalid email address", "reg")
            is_valid = False
        if len(request["password"]) < 1:
            is_valid = False
            flash("Please provide password", "reg")
        elif len(request["confirm_password"]) < 1:
            is_valid = False
            flash("Please confirm password", "reg")
        print(request["password"])
        print(request["confirm_password"])
        if request["password"] != request["confirm_password"]:
            is_valid = False
            flash("Passwords do not match", "reg")
        print(is_valid)
        return is_valid




    # Create Users Models



    # Read Users Models



    # Update Users Models



    # Delete Users Models