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

@app.route('/ninjas/<int:id>/delete')
def deleteNinja(id):
    data = {
        "id" : id
    }
    ninja.Ninja.destroy(data)
    return redirect('/dojos')

@app.route('/ninjas/<int:id>/update')
def updateNinja(id):
    data = {
        "id" : id
    }
    return render_template('edit.html', ninja = ninja.Ninja.getOne(data))

@app.route('/ninjas/update', methods=["POST"])
def updateSubmit():
    ninja.Ninja.update(request.form)
    return redirect('/dojos')