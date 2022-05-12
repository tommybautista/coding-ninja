from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models import dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def showDojos():
    return render_template("dojos.html")


@app.route('/dojos/submit', methods=["POST"])
def createNinja():
    if not dojo.Dojo.valid(request.form):
        return redirect('/')
    dojo.Dojo.save(request.form)
    return redirect('/dojos/results')

@app.route('/dojos/results')
def results():
    return render_template("results.html", dojos = dojo.Dojo.get_last_survey())