from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models import dojo, ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def showDojos():
    return render_template("dojos.html", dojos=dojo.Dojo.getAll())

@app.route('/newDojo', methods=["POST"])
def newDojo():
    data = {
        "name" : request.form["name"]
    }
    dojo.Dojo.save(data)
    return render_template("dojos.html", dojos=dojo.Dojo.getAll())

@app.route('/dojos/<int:id>/destroy')
def delete(id):
    data = {
        "id" : id
    }
    dojo.Dojo.destroy(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>/view')
def dojosView(id):
        data = {
        "id" : id
        }
        return render_template("dojos-n-ninjas.html", dojo=dojo.Dojo.get_one_with_ninjas(data))
