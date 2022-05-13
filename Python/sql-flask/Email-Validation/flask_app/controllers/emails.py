from flask import Flask, redirect, render_template, request, session
from flask_app import app
from flask_app.models import email

@app.route('/')
def index():
    return render_template("emailvalidation.html") 

@app.route('/email/register', methods=['POST'])
def registration():
    register_data = {
        "email" : request.form['email'],
    }
    user_id = email.Email.register_email(register_data)
    return redirect("emailvalidationsuccess.html")

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    # ... do other things
    return redirect('/dashboard')
