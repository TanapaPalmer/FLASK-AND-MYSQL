from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo


class Ninja:

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.owner = None
    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        results = connectToMySQL('dojos_and_ninjas_2_schema').query_db(query,data)
        return results

    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE ninjas.id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_2_schema').query_db(query,data)
        return result

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_2_schema').query_db(query,data)
        return result
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE ninjas.id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_2_schema').query_db(query,data)
        print(result)
        return cls(result[0])