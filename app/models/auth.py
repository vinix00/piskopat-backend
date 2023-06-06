from app.models.db import cursor

class DatabaseControl():
  def register_user(given_username, given_password):
    query = "INSERT INTO user VALUES (NULL, %s, %s, %s, %s)"
    data = (given_username, given_password, "NOW()", 1)
    cursor.execute(query)
    cursor.commit()


dbControl = DatabaseControl()