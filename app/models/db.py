from flask import Flask
import mysql.connector
from mysql.connector import errorcode
 
app = Flask(__name__)

try:
  cnx = mysql.connector.connect(user='root',
                              host='localhost',
                              database='piskodb')

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

db = cnx.cursor(buffered=True)