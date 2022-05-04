from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users/')

@app.route('/users/')
def users():
    print("all users from controller file: ", User.getAll())
    return render_template('users.html', users=User.getAll())

@app.route('/users/submit/', methods=["POST"])
def submitNew():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/')
    
@app.route('/users/create')
def addNew():
    return render_template('create.html')