from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    db = 'dojos_and_ninjas'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

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
        query = 'INSERT INTO ninjas (first_name, last_name, age) VALUES (%(first_name)s, %(last_name)s, %(age)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def getCohort(cls, data):
        # Here is where join statements will go to show all the cohorts for one subject
        pass


