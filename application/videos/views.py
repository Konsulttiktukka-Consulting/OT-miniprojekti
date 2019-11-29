from flask import Blueprint, flash, g, redirect, render_template, request, url_for

from application import db
from application.videos.models import Video
from application.videos.forms import VideoForm

bp = Blueprint("videos", __name__)


@bp.route("/videos/new/")
def video_form():
    form = VideoForm()
    return render_template("videos/new.html", form=form)
