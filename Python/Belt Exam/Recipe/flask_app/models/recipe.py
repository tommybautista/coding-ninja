from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Recipe:
    db = "recipe"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = []

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM recipes;'
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for row in results:
            recipes.append(cls(row))
        print(recipes)
        return recipes

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM recipes WHERE id = %(id)s;'
        results =  connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO recipes (name, description, instruction, under_30, user_id) VALUES (%(name)s, %(description)s, %(instruction)s, %(under_30)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE recipes SET name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, password = %(password)s, recipe_id = %(recipe_id)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

