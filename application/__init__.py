from flask import Flask
app = Flask(__name__)

from application import views

from flask_sqlalchemy import SQLAlchemy


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from flask_sqlalchemy import SQLAlchemy

from application.books import models
from application.books import views 

db.create_all()
