from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    db = 'dojo_survey'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_ninja(ninja):
        is_valid = True # we assume this is true
        if len(ninja['name']) < 3:
            flash("Name must be at least 3 characters.")
        #     is_valid = False
        if ninja['location'] == 'Select a Location':
            flash("Must select a Location")
            is_valid = False
        if (ninja['language']) == 'Select a Language':
            flash("Must select a Language.")
            is_valid = False
        if len(ninja['comment']) < 1:
            flash("Comment must be longer.")
            is_valid = False
        return is_valid