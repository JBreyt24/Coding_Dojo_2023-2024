from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from pprint import pprint
from flask_app.models import user_model

class Post:
    myDB = "flaskoct23erds" 
    def __init__(self, dict):
        self.id = dict["id"]
        self.post_content = dict["post_content"]
        self.created_at = dict["created_at"]
        self.updated_at = dict["updated_at"]
        self.creator_id = dict["creator_id"]
        self.creator = None

    @classmethod
    def get_all_join_creator(cls):
        query = """
        SELECT *
        FROM posts p
        JOIN users u
        ON p.creator_id = u.id;
        """
        list_returned_from_db = connectToMySQL(cls.myDB).query_db(query)
        pprint(list_returned_from_db)
        output = []
        for data in list_returned_from_db:
            this_post = cls(data)
            user_info = {
                'id': data["id"],
                'first_name' : data['first_name'],
                'last_name' : data['last_name'],
                'email' : data['email'],
                'password' : data['password'],
                'created_at' : data['created_at'],
                'updated_at' : data['updated_at'],
            }
            this_user = user_model.User(user_info)
            # print("-----------------")
            # print(each_dictionary)
            # print(cls(each_dictionary))
            this_post.creator = this_user
            output.append(this_post)
        # print(output)
        return output