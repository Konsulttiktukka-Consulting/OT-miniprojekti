import pytest

from application import db

from application.blogposts.models import BlogPost

def test_create(client, app):
    assert client.get("/blogposts/new").status_code == 200
    client.post("/videos/", data={"title": "Eeron blogi",
                                  "url": "http://oontääkissa.com"
    })

    with app.app_context():
        assert BlogPost.query.count() == 1