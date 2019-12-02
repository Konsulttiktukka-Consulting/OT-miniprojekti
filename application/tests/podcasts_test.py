import pytest
from application import db
from application.podcasts.models import Podcast

def test_create(client, app):
    assert client.get("/podcasts/new").status_code == 308
    client.post("/podcasts/", data={"title": "Podcastin otsikko"
     })

    with app.app_context():
        assert Podcast.query.count() == 1