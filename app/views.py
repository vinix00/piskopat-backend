from flask import render_template, redirect, request, session
from app.models.invite_codes import Invite
from app.models.auth import auth
from app import app

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
    invite_code = request.form.get('invite_code')

    if auth.register_user(username, password, invite_code) == True:
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
    if auth.login_user(username, password) == True:
      session['logged_in'] = True
      session['user'] = username
      return redirect("/dashboard")
    else:
      return redirect("/login")

@app.route("/generate_code", methods=['POST', 'GET'])
def generate_code():
  Invite.generate()
  return redirect("/login")
  

@app.route("/logout")
def logout():
  session.pop('user')
  redirect("/login")
  