import pytest
import re
from application import db
from application.videos.models import Video


def test_create(client, app):
    assert client.get("/videos/new/").status_code == 200
    client.post("/videos/", data={"title": "koiravideo",
                                  "url": "https://www.youtube.com/watch?v=h1sRFc5FiZA"})

    with app.app_context():
        assert Video.query.count() == 2
