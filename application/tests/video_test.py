import pytest

from application import db
from application.videos.models import Video


def test_create(client, app):
    assert client.get("/videos/new/").status_code == 200
    client.post("/videos/", data={"title": "koiravideo",
                                  "url": "youtube.com"})

    with app.app_context():
        assert Video.query.count() == 2
