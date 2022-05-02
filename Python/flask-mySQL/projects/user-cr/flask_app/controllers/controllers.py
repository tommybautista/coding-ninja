from flask import redirect, render_template, request, session
from flask_app import app

@app.route('/')                           
def index():
    return render_template("index.html")

@app.route('/')
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("index.html")

    ajhfjgf