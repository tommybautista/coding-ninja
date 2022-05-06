from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users/')

@app.route('/users/')
def users():
    # print("all users from controller file: ", User.getAll())
    return render_template('users.html', users=User.getAll())

@app.route('/users/create')
def create():
    return render_template('create.html')

@app.route('/users/submit/', methods=["POST"])
def submitNew():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/')


@app.route("/users/<int:id>/")
def view(id):
    data = {
        "id" : id
    }
    # print(User.getOne(data))
    return render_template('view.html', user = User.getOne(data))

@app.route('/users/<int:id>/edit')
def edit(id):
    data = {
        "id" : id
    }
    return render_template('edit.html', user = User.getOne(data))

@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/<int:id>/destroy')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/users')


@app.route('/home')
def home():
    return redirect('/')