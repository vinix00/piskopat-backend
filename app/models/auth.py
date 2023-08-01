from app.models.db import db, cnx
from app.models.invite_codes import Invite

class DatabaseControl():
  def register_user(self, given_username, given_password, invite_code):
    if Invite.check(invite_code) == True:
      pass
    else:
      return False
    query1 = ("SELECT username FROM users WHERE username = %s")
    data = (given_username,)
    db.execute(query1, data)
    result = db.fetchone()
    if result == None:
      print("Valid User")
      pass
    else: 
      print("Username vergeben")
      return False
    query2 = ("INSERT INTO users (username, password, join_date, role) VALUES (%s, %s, NOW(), 1)")
    try:
      given_data = given_username, given_password
      db.execute(query2, given_data,)
      cnx.commit()
    except:
      print("Fehler beim erstellen des Users")
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
      print("Login erfolgreich")
      return True

auth = DatabaseControl()