from flask import redirect, render_template, request, session
from flask_app import app

@app.route('/')                           
def index():
    return render_template("index.html")