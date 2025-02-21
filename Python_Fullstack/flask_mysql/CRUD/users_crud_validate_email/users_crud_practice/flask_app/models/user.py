from flask_app.config.mysqlconnection import connectToMySQL
#might need other imports like flash other classes and regex
from flask_app import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

db = 'users_schema'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['data']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #follow database table fields plus any other attribute you want to create

    @staticmethod
    def validate_user(user_info):
        is_valid = True
        if not EMAIL_REGEX.match(user_info['email']):
            flash('Invalid email address')
            is_valid = False
        return is_valid

    @staticmethod
    def is_valid_user(user_info):
        is_valid = True

        if len(user_info['first_name']) < 2:
            flash("First name required")
            is_valid = False
        if len(user_info['last_name']) < 2:
            flash("Last name required")
            is_valid = False
        if len(user_info['email']) < 3:
            flash("Email required")
            is_valid = False
        return is_valid


    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users_schema").query_db(query)
        users = []
        for user_info in results:
            users.append(cls(user_info))
        return users
        #Nice little head start
        #Rest of code here


    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        result = connectToMySQL('users_schema').query_db(query, data)
        return result
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL("users_schema").query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query, data)