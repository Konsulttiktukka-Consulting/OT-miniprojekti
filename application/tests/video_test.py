import pytest
import re
from application import db
from application.videos.models import Video


def test_create(client, app):
    assert client.get("/videos/new/").status_code == 200
