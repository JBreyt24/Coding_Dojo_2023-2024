
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from pprint import pprint
from flask_app.models.post_model import Post
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class User:
    myDB = "flaskoct23erds" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.posts = []
        # What changes need to be made above for this project?
        #What needs to be added here for class association?

    @staticmethod
    def validate_user(request):
        #boolean value for validity
        is_valid = True
        #access request values same way we access request.form
        #
        if len(request['first_name']) < 1:
            is_valid = False
            flash("Please provide first name")
        elif len(request['first_name']) < 3:
            is_valid = False
            flash("First name must be at least 3 characters")
        if len(request['last_name']) < 1:
            is_valid = False
            flash("Please provide last name")
        if len(request['age']) < 1:
            is_valid = False
            flash("Please provide age")
        elif int(request['age']) < 18:
            is_valid = False
            flash("Must be 18 years of age or older")
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
            flash('Password fields should be the same')

        #return value of validity
        print(is_valid)
        return is_valid



    @classmethod
    def get_by_id_join_posts(cls, data):
        query = """
        SELECT * FROM users u
        LEFT JOIN posts p
        ON u.id = p.creator_id
        WHERE u.id = %(id)s;
        """
        list_returned_from_db = connectToMySQL(cls.myDB).query_db(query, data)
        # pprint(list_returned_from_db)
        this_user = cls(list_returned_from_db[0])
        print(this_user.age)
        for each_dictionary in list_returned_from_db:
            #
            #
            #
            print(each_dictionary)
            post_info = {
                'id': each_dictionary["p.id"],
                'post_content' : each_dictionary['post_content'],
                'created_at' : each_dictionary['p.created_at'],
                'updated_at' : each_dictionary['p.updated_at'],
                'creator_id' : each_dictionary['creator_id'],
            }
            #
            this_post = Post(post_info)
            print(this_post)
            #
            this_user.posts.append(this_post)
            #
        return this_user

    @classmethod
    def get_all(cls):
        query = """
        SELECT *
        FROM USERS
        """
        list_returned_from_db = connectToMySQL(cls.myDB).query_db(query)
        # print(list_returned_from_db)
        output = []
        for each_dictionary in list_returned_from_db:
            # print("-----------------")
            # print(each_dictionary)
            # print(cls(each_dictionary))
            output.append(cls(each_dictionary))
        print(output)
        return output


    # Create Users Models


    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, age, email, password)
        VALUES (%(fname)s, %(lname)s, %(age)s, %(email)s, %(pw)s)
        """
        # user_id = connectToMySQL(cls.myDB).query_db(query, data)
        return connectToMySQL(cls.myDB).query_db(query, data)


    # Read Users Models

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


    # Update Users Models

    @classmethod
    def update_by_id(cls, data):
        query = """
        UPDATE users
        SET first_name = %(fname)s,
        last_name = %(lname)s, 
        email = %(email)s
        WHERE id = %(id)s
        """
        connectToMySQL(cls.myDB).query_db(query, data)

    # Delete Users Models

    @classmethod
    def delete_by_id(cls, data):
        query = """
        DELETE 
        FROM users
        WHERE id = %(id)s
        """
        connectToMySQL(cls.myDB).query_db(query, data)