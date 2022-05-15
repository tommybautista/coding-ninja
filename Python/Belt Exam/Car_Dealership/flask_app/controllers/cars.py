from contextlib import redirect_stderr
from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models import car
from flask_app.models.salesperson import Salesperson

@app.route('/cars/<int:id>/new')
def new(id):
    data = {
        "id": id
    }
    session['salesperson_id'] = id
    return render_template("addcar.html", salespersons = Salesperson.getOne(data))

@app.route('/cars/<int:id>/create', methods=["POST"])
def addCars(id):
    x = id
    if not car.Car.validate_car(request.form):
        return redirect(f'/cars/{x}/new')
    car.Car.save(request.form)
    return redirect('/dashboard')

@app.route('/cars/<int:id>/view')
def viewCar(id):
    data = {
        "id" : id
    }
    print(id)
    return render_template("viewcar.html", cars = car.Car.getOne(data))

@app.route('/cars/<int:id>/edit')
def editCar(id):
    x = id

    data = {
        "id" : id
    }
    print(id)
    return render_template("edit.html", cars = car.Car.getOne(data), salespersons = Salesperson.getOne(data))    

@app.route('/cars/<int:id>/update', methods=['POST'])
def carsUpdate(id):
    car.Car.update(request.form)
    return redirect('/dashboard')

@app.route('/cars/<int:id>/destroy')    
def destroyCar(id):
    data = {
        "id" : id
    }
    car.Car.destroy(data)
    return redirect('/dashboard')

@app.route("/cars/<int:id>/purchase")
def purchased(id):
    data = {
        "id" : id
    }
    car.Car.destroy(data)
    return redirect('/dashboard')
