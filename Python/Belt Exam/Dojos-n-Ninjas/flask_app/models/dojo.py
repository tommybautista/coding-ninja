from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    db = 'dojos_and_ninjas'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL(cls.db).query_db(query)
        
        dojos = []
        for row in results:
            dojos.append(cls(row))
        print(dojos)
        return dojos

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM dojos WHERE id = %(id)s;'
        results =  connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE dojos SET name = %(name)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_one_with_ninjas(cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        
        dojo = cls(results[0])
        print(dojo)
        for row in results:
            data = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append( Ninja(data) )
        return dojo