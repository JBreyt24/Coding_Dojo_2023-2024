
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class Ninja:
    myDB = "dojos_DB" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.first_name = ['first_name']
        self.last_name = ['last_name']
        self.age = ['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added here for class association?


    # Create Users Models

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO ninjas (first_name, last_name, age, dojo_id)
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);
        """
        return connectToMySQL(cls.myDB).query_db(query, data)

    # Read Users Models



    # Update Users Models



    # Delete Users Models