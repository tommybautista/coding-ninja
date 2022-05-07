
import re
from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def showDojos():
    return render_template("dojos.html", dojos=Dojo.getAll())

@app.route('/newDojo', methods=["POST"])
def newDojo():
    data = {
        "name" : request.form["name"]
    }
    Dojo.save(data)
    return render_template("dojos.html", dojos=Dojo.getAll())

@app.route('/dojos/<int:id>/destroy')
def delete(id):
    data = {
        "id" : id
    }
    Dojo.destroy(data)
    return redirect('/dojos')

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")

@app.route('/ninjas/create', methods=['POST'])
def createNinja():
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form[ 'age' ],
        "dojo_id" : request.form['dojo_id']
    }
    Ninja.save(data)
    return render_template("ninjas.html", ninjas=Ninja.getAll(), dojos=Dojo.getAll())

@app.route('/dojos/<int:id>/view')
def dojosView(id):
        data = {
        "id" : id
        }
        return render_template("dojos-n-ninjas.html", dojos=Dojo.getOne(data))
