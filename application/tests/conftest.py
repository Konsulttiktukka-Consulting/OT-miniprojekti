from testing.postgresql import Postgresql
import pytest
from application import create_app 
from application import db as db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class TestConfig(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = 'test'


@pytest.yield_fixture(scope='session')
def app():
    _app = create_app(TestConfig)
    _app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tests/test.db" 


    yield _app




@pytest.fixture(scope='session')
def testapp(app):
    return app.test_client()


@pytest.yield_fixture(scope='session',autouse=True)
def _db(app):
    db = SQLAlchemy(app=app)
    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(144), nullable=False)
        author = db.Column(db.String(144), nullable=False)
        description = db.Column(db.String(400), nullable=False)

    db.create_all()

    yield db
    db.session().close()
    db.drop_all()