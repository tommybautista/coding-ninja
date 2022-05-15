from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.car import Car
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Salesperson: 
    db = 'Car_Dealership'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.cars = []

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM salespersons;'
        results = connectToMySQL(cls.db).query_db(query)
        salespersons = []
        for row in results:
            salespersons.append(cls(row))
        print(salespersons)
        return salespersons

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM salespersons WHERE id = %(id)s;'
        results =  connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO salespersons (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE salespersons SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, password = %(password)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM salespersons WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    #This is for JOINING tables
    @classmethod
    def get_one_with_cars(cls, data ):
        query = "SELECT * FROM salespersons LEFT JOIN cars ON cars.salesperson_id = salespersons.id WHERE salespersons.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        
        salesperson = cls(results[0])
        print(salesperson)
        for row in results:
            data = {
                'id': row['cars.id'],
                'price': row['price'],
                'year': row['year'],
                'make': row['make'],
                'model': row['model'],
                'description': row['description'],
                'seller': row['seller'],
                'created_at': row['cars.created_at'],
                'updated_at': row['cars.updated_at']
            }
            salesperson.cars.append(Car(data))
        return salesperson


    @classmethod
    def get_salesperson_by_email(cls, data):
        query = "SELECT * FROM salespersons WHERE email = %(email)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False        
        salesperson = cls(results[0])
        return salesperson

    @staticmethod
    def validate_register(salesperson):
        is_valid = True
        salesperson_in_db = Salesperson.get_salesperson_by_email(salesperson)
        if salesperson_in_db:
            flash("Email is associated with another account")
            is_valid = False
        if len(salesperson['first_name']) < 3:
            flash("First Name must be at least 3 characters", "error")
            is_valid = False
        if len(salesperson['last_name']) < 3:
            flash("Last Name must be at least 3 characters", "error")
            is_valid = False
        if not EMAIL_REGEX.match(salesperson['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(salesperson['password']) < 8:
            flash("Password must be at least 8 characters", "error")
            is_valid = False
        if salesperson['password'] != salesperson['confirm_password']:
            flash("Password must match", "error")
            is_valid = False            
        return is_valid

    @staticmethod
    def validate_login(salesperson):
        is_valid = True
        salesperson_in_db = Salesperson.get_salesperson_by_email(salesperson)
        if not salesperson_in_db:
            flash("Email is not associated with another account")
            is_valid = False        
        if not EMAIL_REGEX.match(salesperson['email']): 
            flash("Invalid email address!")
            is_valid = False          
        return is_valid