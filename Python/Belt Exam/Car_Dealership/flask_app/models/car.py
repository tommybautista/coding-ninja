from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import salesperson
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Car:
    db = "car_dealership"
    def __init__(self, data):
        self.id = data['id']
        self.price = data['price']
        self.year = data['year']
        self.make = data['make']
        self.model = data['model']
        self.description = data['description']
        self.seller = data['seller']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM cars;"
        results =  connectToMySQL(cls.db).query_db(query)
        all_cars = []
        for row in results:
            all_cars.append( cls(row) )
        return all_cars

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM cars WHERE id = %(id)s;'
        results =  connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO cars (price, year, make, model, description, seller, salesperson_id) VALUES (%(price)s, %(year)s, %(make)s, %(model)s,%(description)s, %(seller)s, %(salesperson_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE cars SET price = %(price)s, year = %(year)s, make = %(make)s, model = %(model)s, description = %(description)s, seller = %(seller)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM cars WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_car(car):
        is_valid = True
        if int(car['price']) == 0:
            flash("Price must be higher than $0.")
            is_valid = False
        if int(car['year']) < 2000:
            flash("Car must be newer that 2000.")
            is_valid = False  
        if len(car['make']) < 2:
            flash("Make must be at least 2 characters.")                 
        if len(car['model']) < 2:
            flash("Model must be at least 2 characters.")
            is_valid = False
        return is_valid