import random
from flask import redirect, render_template, request, session
from flask_app import app

@app.route('/')                           
def index():
    session['random_number'] = random.randint(1,100+1)
    print(session['random_number'])
    if 'count' not in session:
        session['count'] = 0
    # else:
    #     session['count'] += 1
    return render_template("index.html")

@app.route('/guess', methods=['POST'])                           
def guess():
    session['count'] += 1
    session['guess'] = request.form['guess']
    return redirect('/results')    

@app.route('/results')                           
def result():
    if session['count'] >= int(5):
        return render_template("lose.html")
    elif int(session['guess']) < int(session['random_number']):
        return render_template("too_low.html")
    elif int(session['guess']) > int(session['random_number']):
        return render_template("too_high.html")
    else: 
        return render_template("correct.html")

@app.route('/submit', methods=['POST'])                           
def submit():
    session['name'] = request.form['name']
    return redirect('/leadersboard') 

@app.route('/leadersboard')                    
def leadersboard():
    return render_template("leadersboard.html")  


@app.route('/clear')                           
def clear():
    session.pop('count')
    return redirect('/')