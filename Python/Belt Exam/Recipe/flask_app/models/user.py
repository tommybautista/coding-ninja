from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user, recipe
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "recipe"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users(first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);" 
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        user = cls(results[0])
        return user

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False        
        user = cls(results[0])
        return user

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users LEFT JOIN recipes ON recipes.user_id = users.id WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        
        user = cls(results[0])
        print(user)
        for row in results:
            data = {
                'id': row['recipes.id'],
                'name': row['name'],
                'description': row['description'],
                'instruction': row['instruction'],
                'under_30': row['under_30'],
                'created_at': row['recipes.created_at'],
                'updated_at': row['recipes.updated_at'],
                'user_id' : row['user_id']
            }
            user.recipes.append(recipe.Recipe(data))
        return user

    @staticmethod
    def validate_register(user):
        is_valid = True
        user_in_db = User.get_user_by_email(user)
        if user_in_db:
            flash("Email is associated with another account")
            is_valid = False
        if len(user['first_name']) < 3:
            flash("First Name must be at least 3 characters", "error")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last Name must be at least 3 characters", "error")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters", "error")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Password must match", "error")
            is_valid = False            
        return is_valid

    @staticmethod
    def validate_login(user):
        is_valid = True
        user_in_db = User.get_user_by_email(user)
        if not user_in_db:
            flash("Email is not associated with another account")
            is_valid = False        
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False          
        return is_valid