from crypt import methods
from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.recipe import Recipe


@app.route('/recipes/view')
def view():
    return render_template("viewrecipe.html")

@app.route('/recipes/<int:id>/new')
def new():
    return render_template("addrecipe.html")

@app.route("/recipes/create", methods=['POST'])
def create(id):
    data = {
        "id" : request.form['id'],
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instruction" : request.form['instruction'],
        "under_30" : request.form['under_30']
    }
    Recipe.save(data)
    return redirect('/dashboard')


@app.route('/ninjas/<int:dojoID>/<int:id>/delete')
def deleteNinja(dojoID,id):
    data = {
        "id" : id
    }
    x = dojoID
    ninja.Ninja.destroy(data)  
    return redirect(f'/dojos/{x}/view')