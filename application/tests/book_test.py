import pytest
from flask import url_for

from application import db
from application.books.models import Book


def test_index(client):
    response = client.get("/")
    assert b"Hello world!" in response.data


def test_create(client, app):
    assert client.get("/books/new/").status_code == 200
    client.post("/books/", data={"title": "moi",
                                 "author": "moi", "description": "moi"})

    with app.app_context():
        assert Book.query.count() == 2


def test_bookmarkList(client, app):
    res = client.get("/books")
    assert res.status_code == 200
    assert b"List of bookmarks" in res.data


def test_update(client, app):
    res = client.get("/books/update/1/")
    assert res.status_code == 200
    assert b"Updating book" in res.data


