from flask import Blueprint, flash, g, redirect, render_template, request, url_for

from application import db
from application.videos.models import Video
from application.videos.forms import VideoForm

bp = Blueprint("videos", __name__)


@bp.route("/videos/new/")
def video_form():
    form = VideoForm()
    return render_template("videos/new.html", form=form)


@bp.route("/videos/", methods=["GET", "POST"])
def videos_create():
    form = VideoForm(request.form)
    if form.validate_on_submit():
        newBook = Video(form.title.data, form.url.data)
        db.session().add(newBook)
        db.session().commit()
        return redirect(url_for("books.books_index"))

    return render_template("videos/new.html", form=form)


@bp.route("/videos/<video_id>/update", methods=["GET", "POST"])
def videos_update(video_id):
    video = Video.query.get(video_id)
    form = VideoForm()
    if form.validate_on_submit():
        form.populate_obj(video)
        db.session().commit()
        return redirect(url_for("books.books_index"))

    form = VideoForm(obj=video)
    return render_template("videos/update.html", video=video, form=form)


@bp.route("/videos/<video_id>", methods=["GET", "POST"])
def videos_show(video_id):
    video = Video.query.get(video_id)
    return render_template("videos/video.html", video=video)
