
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_model import User
from flask import flash, request



class Recipe:
    myDB = 'recipes_schema'
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.date = data['date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.cook = None
        

# Create Recipe

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO recipes (user_id, name, description, instructions, under_30, date)
        VALUES (%(user_id)s, %(name)s, %(description)s, %(instructions)s, %(under_30)s, %(date)s);
        """
        return connectToMySQL(cls.myDB).query_db(query, data)
    
    @staticmethod
    def validate_recipe_at_create(recipe_form_data):
        is_valid = True
        if len(recipe_form_data['name']) < 3:
            flash('Name must be at least 3 characters', "recipe")
            is_valid = False
        if len(recipe_form_data['description']) < 3:
            flash('Description must be at least 3 characters', "recipe")
            is_valid = False
        if len(recipe_form_data['instructions']) < 3:
            flash('Instructions must be at least 3 characters', "recipe")
            is_valid = False
        if (recipe_form_data['date']) == '':
            flash('Please submit a date', "recipe")
            is_valid = False
        if 'under_30' not in request.form :
            flash('Please select for "Under 30 mins?"', "recipe")
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_recipe_at_edit(recipe_form_data):
        is_valid = True
        if len(recipe_form_data["name"]) < 3:
            flash('Name must be at least 3 characters', "recipe_edit")
            is_valid = False
        if len(recipe_form_data['description']) < 3:
            flash('Description must be at least 3 characters', "recipe_edit")
            is_valid = False
        if len(recipe_form_data['instructions']) < 3:
            flash('Instructions must be at least 3 characters', "recipe_edit")
            is_valid = False
        if (recipe_form_data['date']) == '':
            flash('Please submit a date', "recipe_edit")
            is_valid = False
        if 'under_30' not in request.form:
            flash('Please select for "Under 30 mins?"', "recipe_edit")
            is_valid = False
        return is_valid

# Read Recipe

    @classmethod
    def get_one(cls, recipe_id):
        query = """
        SELECT * FROM recipes
        WHERE id = %(id)s;
        """
        data = {
            'id': recipe_id
            }
        results = connectToMySQL(cls.myDB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_all_recipes_w_user(cls):
        query = """
        SELECT * FROM recipes
        LEFT JOIN users ON recipes.user_id = users.id
        """
        results = connectToMySQL(cls.myDB).query_db(query)
        recipes_by_user = []
        for recipe in results:
            one_recipe =cls(recipe)
            cook_dict = {
                'id': recipe["users.id"],
                'first_name':recipe['first_name'],
                'last_name' : recipe['last_name'],
                'email' : recipe['email'],
                'password' : None,
                'created_at' : recipe['users.created_at'],
                'updated_at' : recipe['users.updated_at']
            }
            one_recipe.cook = User(cook_dict)
            recipes_by_user.append(one_recipe)
        return recipes_by_user
    
# Update Recipe

    @classmethod
    def edit_recipe(cls, data):
        query = """
        UPDATE recipes
        SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date = %(date)s, under_30 = %(under_30)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.myDB).query_db(query,data)
    
# Delete Recipe

    @classmethod
    def destroy_recipe(cls, recipe_id):
        query = """ 
        DELETE FROM recipes
        WHERE id = %(id)s;
        """
        data = {
            "id" : recipe_id
        }
        return connectToMySQL(cls.myDB).query_db(query, data)