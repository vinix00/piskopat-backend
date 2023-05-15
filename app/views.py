from app import app

from flask import render_template

@app.route("/")
def index():
  return render_template('public/index.html')

@app.route("/register")
def register():
  return render_template('public/register.html')

@app.route("/login")
def login():
  return render_template('public/login.html')