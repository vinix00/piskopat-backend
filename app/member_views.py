from app import app
from flask import render_template, request, session, redirect

from flask import render_template

@app.route('/dashboard')
def dashboard():
  if session.get('logged_in') == True:
    return render_template('member/dashboard.html')
  else:
    return redirect("/login")