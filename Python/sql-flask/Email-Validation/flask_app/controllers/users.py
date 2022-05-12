import re
from flask import Flask, redirect, render_template, request, session
from flask_app import app

@app.route('/')
def index():
    return render_template("emailvalidation.html")