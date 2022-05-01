from flask import redirect, render_template, request, session
from flask_app import app

@app.route('/')                           
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])                           
def submit():
    session['user_name'] = request.form['name']
    session['user_location'] = request.form['location']
    session['user_language'] = request.form['language']
    session['user_comments'] = request.form['comments']
    return redirect('/process')

@app.route('/process')                           
def process():
    return render_template("process.html")
