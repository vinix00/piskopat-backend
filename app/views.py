from app import app
from time import sleep

from flask import render_template, request, session, redirect

from app.models.auth import dbControl

@app.route("/")
def index():
  return redirect("/login")

@app.route("/register")
def register():
  return render_template('public/register.html')

@app.route("/register-post", methods = ['POST', 'GET'])
def register_post():
  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')

    #invite_code = request.form.get('invite_code')
    if dbControl.register_user(username, password) == True:
      session['logged_in'] = True
      session['user'] = username
      return redirect("/dashboard")
    else:
      return redirect("/register")

@app.route("/login")
def login():

  return render_template('public/login.html')

@app.route("/login-post", methods=['POST'])
def login_post():
  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    if dbControl.login_user(username, password) == True:
      session['logged_in'] = True
      session['user'] = username
      return redirect("/dashboard")
    else:
      return redirect("/login")
  

@app.route("/logout")
def logout():
  session.pop('user')
  redirect("/login")
  