
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.


class User:
    db = "users" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        # self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added here for class association?

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Create Users Models

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email)
        VALUES (%(first_name)s, %(last_name)s, %(email)s)
        """
        return connectToMySQL(cls.db).query_db(query, data)


    # Read Users Models

    @classmethod
    def get_all(cls):
        query = """SELECT * 
        FROM users;
        """
        list_returned_from_db = connectToMySQL(cls.db).query_db(query)
        output = []
        for each_dictionary in list_returned_from_db:
            output.append(cls(each_dictionary))
        print(output)
        return output
    
    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM users 
        WHERE id = %(id)s
        """
        result = connectToMySQL(cls.db).query_db(query, data)
        print(result)
        return cls(result[0])

    # Update Users Models

    @classmethod
    def update(cls, data):
        query = """UPDATE users 
        SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s,
        updated_at = NOW()
        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)
    
    # Delete Users Models

    @classmethod
    def destroy(cls, data):
        query = """ DELETE FROM users
        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)