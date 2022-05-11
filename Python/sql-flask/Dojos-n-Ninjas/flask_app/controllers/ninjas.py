from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html", dojos = dojo.Dojo.getAll())

@app.route('/ninjas/create', methods=["POST"])
def createNinja():
    if not ninja.Ninja.validate_ninja(request.form):
        return redirect('/ninjas')
    ninja.Ninja.save(request.form)
    return redirect('/dojos')

@app.route('/ninjas/<int:dojoID>/<int:id>/delete')
def deleteNinja(dojoID,id):
    data = {
        "id" : id
    }
    x = dojoID
    ninja.Ninja.destroy(data)  
    return redirect(f'/dojos/{x}/view')


@app.route('/ninjas/<int:dojoID>/<int:id>/update')
def updateNinja(dojoID, id):
    data = {
        "id" : id
    }
    dojo_data = {
        "id" : dojoID
    }
    return render_template('edit.html', ninja = ninja.Ninja.getOne(data), dojo = dojo.Dojo.getOne(dojo_data))

@app.route('/ninjas/<int:id>/update', methods=["POST"])
def updateSubmit(id):
    ninja.Ninja.update(request.form)
    x = id
    return redirect(f'/dojos/{x}/view')