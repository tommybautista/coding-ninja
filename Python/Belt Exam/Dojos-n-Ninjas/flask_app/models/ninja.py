from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Ninja:
    db = 'dojos_and_ninjas'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM ninjas;'
        results = connectToMySQL(cls.db).query_db(query)
        ninjas = []
        for row in results:
            ninjas.append(cls(row))
        return ninjas

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM ninjas WHERE id = %(id)s;'
        results =  connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_ninja(ninja):
        is_valid = True # we assume this is true
        if len(ninja['first_name']) < 3:
            flash("First Name must be at least 3 characters.")
            is_valid = False
        if len(ninja['last_name']) < 3:
            flash("Last Name must be at least 3 characters.")
            is_valid = False
        if int(ninja['age']) < 18:
            flash("Ninja must be 18 or older.")
            is_valid = False
        return is_valid


