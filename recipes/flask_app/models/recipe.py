from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask_app.models import recipe
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.datemade = data['datemade']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.creator = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users on recipes.user_id = users.id;"
        results = connectToMySQL('recipes').query_db(query)
        recipes = []
        for row in results:
            one_recipe = cls(row)
            user_data = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": "",
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            one_recipe.creator = user.User(user_data)
            recipes.append(one_recipe)
        return recipes
    
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM recipes JOIN users on recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        result = connectToMySQL('recipes').query_db(query,data)
        if not result:
            return False

        result = result[0]
        this_recipe = cls(result)
        data = {
                "id": result['users.id'],
                "first_name": result['first_name'],
                "last_name": result['last_name'],
                "email": result['email'],
                "password": "",
                "created_at": result['users.created_at'],
                "updated_at": result['users.updated_at']
        }
        this_recipe.creator = user.User(data)
        return this_recipe

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name,description,instructions,datemade,under_30,user_id) VALUES (%(name)s,%(description)s,%(instructions)s,%(datemade)s,%(under_30)s,%(user_id)s);"
        return connectToMySQL('recipes').query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, datemade = %(datemade)s, under_30 = %(under_30)s WHERE id = %(id)s;"
        return connectToMySQL('recipes').query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('recipes').query_db(query,data)
    
    @staticmethod
    def validate_recipe(data):
        is_valid = True

        if len(data['name']) < 3:
            flash("Name must be at least 3 characters long.")
            is_valid = False
        if len(data['description']) < 3:
            flash("Description must be at least 3 characters long.")
            is_valid = False
        if len(data['instructions']) < 3:
            flash("Instructions must be at least 3 characters long.")
            is_valid = False
        if ['datemade'] == '':
            flash("Please input a date.")
            is_valid = False
        if 'under_30' not in data:
            flash("Please provide a cook time.")
            is_valid = False

        return is_valid