
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from pprint import pprint
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.


class User:
    myDB = "login_and_reg" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        # self.age = data['age']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added here for class association?


    # Create Users Models

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        return connectToMySQL(cls.myDB).query_db(query, data)
    

    @staticmethod
    def validate_user(request):
        is_valid = True

        if len(request['first_name']) < 1:
            is_valid = False
            flash("Please provide first name")
        elif len(request['first_name']) < 3:
            is_valid = False
            flash("First name must be at least 3 characters")

        if len(request['last_name']) < 1:
            is_valid = False
            flash("Please provide last name")
        elif len(request['last_name']) < 3:
            is_valid = False
            flash("Last name must be at least 3 characters")

        # if len(request['age']) < 1:
        #     is_valid = False
        #     flash("Please provide age")
        # elif int(request['age']) < 18:
        #     is_valid = False
        #     flash("Must be 18 years of age or older")

        if len(request['email']) < 1:
            is_valid = False
            flash("Please provide email")
        elif not EMAIL_REGEX.match(request['email']): 
            flash("Invalid email address")
            is_valid = False
            return is_valid
        
        if len(request['password']) < 1:
            is_valid = False
            flash("Please provide password")
        elif len(request['confirm_password']) < 1:
            is_valid = False
            flash("Please confirm password")

        print(request['password'])
        print(request['confirm_password'])
        if request['password'] != request['confirm_password']:
            is_valid = False
            flash('Passwords should be the same')

        print(is_valid)
        return is_valid
    
    
    @classmethod
    def get_by_id(cls, data):
        query = """
        SELECT * FROM users 
        WHERE id = %(id)s
        """
        list_returned_from_db = connectToMySQL(cls.myDB).query_db(query, data)
        # print(list_returned_from_db)
        return cls(list_returned_from_db[0])
    

    @classmethod
    def get_by_email(cls, data):
        query = """
        SELECT * FROM users
        WHERE email = %(email)s;
        """
        result = connectToMySQL(cls.myDB).query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])




    # Read Users Models



    # Update Users Models

    
    # @classmethod
    # def rename(cls):
    #     query = """
    #     SELECT * FROM users;
    #     """
    #     results = connectToMySQL(cls.myDB).query_db(query)
    #     print(results)
    #     return cls(results[0])



    # Delete Users Models