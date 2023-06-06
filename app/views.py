from app import app

from flask import render_template, request

from app.models.auth import dbControl

@app.route("/")
def index():
  return render_template('public/index.html')

@app.route("/register")
def register():
  return render_template('public/register.html')

@app.route("/register-post")
def register_post():
  username = request.form.get('username')
  password = request.form.get('password')
  dbControl.register_user(username, password)
  
  return render_template('public/register.html')

@app.route("/login")
def login():
  return render_template('public/login.html')

@app.route("/login-post", methods=['POST'])
def login_post():
  username = request.form.get('username')
  password = request.form.get('password')
  print(username, password)
  return render_template('member/dashboard.html')