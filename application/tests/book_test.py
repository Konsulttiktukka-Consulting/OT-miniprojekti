import pytest

from application import db
from application.books.models import Book


def test_index(client):
    response = client.get("/")
    assert b"Hello world!" in response.data


def test_create(client, app):
    assert client.get("/books/new/").status_code == 200
    client.post("/books/", data={"name": "moi",
                                 "author": "moi", "description": "moi"})

    with app.app_context():
        assert Book.query.count() == 2
