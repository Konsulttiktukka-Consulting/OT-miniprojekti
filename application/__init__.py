from flask import Flask
app = Flask(__name__)

from application import views

from flask_sqlalchemy import SQLAlchemy

import os



if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)


from application.books import models
from application.books import views 

try:
    db.create_all()
except:
    pass