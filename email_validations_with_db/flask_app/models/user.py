from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def is_valid_user(user_info):
        is_valid = True
        if len(user_info["first_name"]) <= 0:
            flash("First name required")
            is_valid = False
        if len(user_info["last_name"]) <= 0:
            flash("Last name required")
            is_valid = False
        if len(user_info["email"]) <= 0:
            flash("Email required")
            is_valid = False
        if not EMAIL_REGEX.match(user_info["email"]):
            flash("Invalid email address.")
            is_valid = False
        return is_valid


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('email_valid').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL('email_valid').query_db(query, data)
        
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('email_valid').query_db(query,data)
        return cls(results[0])