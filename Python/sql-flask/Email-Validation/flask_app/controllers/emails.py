from flask import Flask, redirect, render_template, request, session
from flask_app import app
from flask_app.models import email

@app.route('/')
def index():
    return render_template("emailvalidation.html") 

@app.route('/email/register', methods=['POST'])
def registration():
    if not email.Email.validate_user(request.form):
        return redirect('/')
    data = {
        "email" : request.form['email']
    }
    email.Email.register_email(data)
    return redirect ('/email/validated')

@app.route('/email/validated')
def validated():
    return render_template("emailvalidationsuccess.html", emails=email.Email.getAll())

@app.route('/email/<int:id>/delete')
def delete(id):
    data = {
        "id" : id
    }
    email.Email.destroy(data)
    return redirect('/email/validated')