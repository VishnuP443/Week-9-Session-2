from flask import flash, redirect, render_template, request, url_for
from app import app



@app.route('/')
def index():
    return render_template("home.html", title="Hello World")