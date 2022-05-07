from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html", dojos = dojo.Dojo.getAll())

@app.route('/ninjas/create', methods=["POST"])
def createNinja():
    ninja.Ninja.save(request.form)
    return redirect('/dojos')