from flask import redirect, render_template, request, session
from flask_app import app

@app.route('/')                           
def index():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/increment')                           
def increment():
    session['count'] += (int(session['numbers'])-1)
    return redirect('/')

@app.route('/clear')                           
def clear():
    session.clear()
    return redirect('/')

@app.route('/provide', methods=['POST'])
def provide():
    session['numbers'] = request.form['numbers']
    return redirect('/')

