
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from .ninja_model import Ninja
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class Dojo:
    myDB = "dojos_DB" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        # What changes need to be made above for this project?
        #What needs to be added here for class association?



    # Create Users Models

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO dojos (name)
        VALUES (%(name)s);
        """
        return connectToMySQL(cls.myDB).query_db(query, data)

    # Read Users Models

    @classmethod
    def get_all(cls):
        query = """
        SELECT *
        FROM dojos;
        """
        results = connectToMySQL(cls.myDB).query_db(query)
        print(results)
        dojos = []
        for d in results:
            dojos.append(cls(d))
        print(results)
        return results
    
    @classmethod
    def get_one_with_ninjas(cls, data):
        query = """
        SELECT * FROM  dojos
        LEFT JOIN ninjas on dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(cls.myDB).query_db(query, data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            n = {
            "id": row['ninjas.id'],
            "first_name":  row['first_name'],
            "last_name": row['last_name'],
            "age": row ['age'],
            "created_at": row ['ninjas.created_at'],
            "updated_at": row['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(n))
        return dojo

    # Update Users Models



    # Delete Users Models