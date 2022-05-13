from flask import Flask, render_template, redirect, request_started, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 

@app.route('/')
def log_and_reg():
    return render_template("login_register.html")

@app.route('/users/login', methods=['POST'])
def login():
    if not User.validate_login(request.form):
        return redirect('/')

    user_data = {
        'email' : request.form['email']
    }
    user = User.get_user_by_email(user_data)
    if user:
        if not bcrypt.check_password_hash(user.password, request.form['password']):
            flash('Email/Password combination is incorrect')
            return redirect('/')
        session['user_id'] = user.id
        flash("Login was successful!", 'info')
        return redirect('/dashboard')
    flash('Email is not tied to account')
    return redirect ('/')

@app.route('/users/register', methods=['POST'])
def registration():
    if not User.validate_register(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    register_data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : pw_hash
    }
    user_id = User.register_user(register_data)
    session['user_id'] = user_id
    flash("Registration was successful!", 'info')
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    user_data = {
        "id" : session['user_id']
    }
    user = User.get_user_by_id(user_data)
    return render_template('dashboard.html', user=user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')