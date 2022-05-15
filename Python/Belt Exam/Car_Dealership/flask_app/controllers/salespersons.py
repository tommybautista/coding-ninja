from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.salesperson import Salesperson
from flask_app.models.car import Car
from flask import flash
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 

@app.route('/')
def index():
    return render_template("login_register.html")

@app.route('/salespersons/login', methods=['POST'])
def login():
    if not Salesperson.validate_login(request.form):
        return redirect('/')
    salesperson_data = {
        'email' : request.form['email']
    }
    salesperson = Salesperson.get_salesperson_by_email(salesperson_data)
    if salesperson:
        if not bcrypt.check_password_hash(salesperson.password, request.form['password']):
            flash('Email/Password combination is incorrect')
            return redirect('/')
        session['salesperson_id'] = salesperson.id
        flash("Login was successful!", 'info')
        return redirect('/dashboard')
    flash('Email is not tied to account')
    print(Salesperson.id)
    return redirect ('/')    

@app.route('/salespersons/register', methods=['POST'])
def registration():
    if not Salesperson.validate_register(request.form):
        return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = Salesperson.save(data)
    session['salesperson_id'] = id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    salesperson_data = {
        "id" : session['salesperson_id']
    }
    salesperson = Salesperson.get_one_with_cars(salesperson_data)
    return render_template('dashboard.html', salesperson=salesperson, cars=Car.getAll())

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')