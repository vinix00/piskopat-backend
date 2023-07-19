from flask import Flask

app = Flask(__name__, static_folder='static')

from app import views
from app import member_views
#from app import models

app.secret_key = "cg47t007ngcg7c47gg7"
