import pytest
from application.videos.models import Video
from application import init_db


def test_init_db_initialises_db_with_one_video(app, client):

    with app.app_context():
        init_db()
        videos = Video.query.all()
        assert videos[1].title == "DreamHackCS"
