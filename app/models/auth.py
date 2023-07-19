from app.models.db import db, cnx
#from app.models.invite_code import InviteCodeControl
from flask import session, redirect
from datetime import date, datetime

class DatabaseControl():
  def register_user(self, given_username, given_password):
    query1 = ("SELECT username FROM users WHERE username = %s")
    data = (given_username,)
    db.execute(query1, data)
    result = db.fetchone()
    if result == None:
      pass
    else: 
      return redirect("/register")
    query2 = ("INSERT INTO users (username, password, join_date, role) VALUES (%s, %s, NOW(), 1)")
    try:
      given_data = given_username, given_password
      db.execute(query2, given_data,)
      cnx.commit()
    except:
      return False
    return True

  def login_user(self, given_username, given_password):
    data = given_username, given_password
    query = ("SELECT username FROM users WHERE username = %s AND password = %s")
    db.execute(query, data,)
    result = db.fetchone()
    if result == None:
      return False
    else:
      return True

  def check_invite_code(given_username, invite_code):
 
    return

dbControl = DatabaseControl()