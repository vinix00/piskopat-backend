from app.models.utils import generate_code
from app.models.db import db, cnx
class Invite:
  def generate():
    new_code = ("pisko-" + generate_code(),)
    print(new_code)
    query = ("INSERT INTO invite_codes VALUES (NULL, %s)")
    db.execute(query, new_code,)
    cnx.commit()
    return
    
  def delete(self):

    pass

  def check(invite_code):
    data = (invite_code,)
    query = ("SELECT code FROM invite_codes WHERE code = %s")
    db.execute(query, data,)
    result = db.fetchone()
    if result == None:
      print("Invite Code existiert nicht")
      return False
    else:
      print("Invite Code existiert")
      return True

invite = Invite()