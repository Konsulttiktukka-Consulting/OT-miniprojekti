from dotenv import load_dotenv
import googleapiclient.discovery
import os
from application.videos.forms import VideoForm
from application.videos.models import Video
from application import db
import re
import json
from flask import Blueprint, flash, g, redirect, render_template, request, url_for
import flask

load_dotenv()

bp = Blueprint("videos", __name__)


@bp.route("/videos/new/")
def video_form():
    form = VideoForm()
    return render_template("videos/new.html", form=form)


@bp.route("/videos/", methods=["POST"])
def videos_create():

    if flask.request.method == 'POST':
        form = VideoForm(request.form)

        if form.validate_on_submit():
            try:
                api_service_name = "youtube"
                api_version = "v3"
                DEVELOPER_KEY = os.getenv("API_KEY")

                youtube = googleapiclient.discovery.build(
                    api_service_name, api_version, developerKey=DEVELOPER_KEY)

                video_id = form.url.data[-11:]

                res = youtube.videos().list(
                    part="snippet",
                    id=video_id
                )
                response = res.execute()
                data = response["items"][0]

                url = data["id"]
                title = data["snippet"]["title"]
                description = data["snippet"]["description"]
                creator = data["snippet"]["channelTitle"]
                platform = "youtube"

                new_video = Video(title, url, creator, description, platform)
                print()
                db.session().add(new_video)
                db.session.commit()

                return redirect(url_for("videos.videos_index"))
            except:
                return render_template("videos/new.html", form=form)
    return render_template("videos/new.html", form=form)


@bp.route("/videos/remove/<video_id>", methods=["POST"])
def remove_video(video_id):
    video = Video.query.get(video_id)
    db.session().delete(video)
    db.session().commit()

    return redirect(url_for("videos.videos_index"))


@bp.route("/videos", methods=["GET"])
def videos_index():
    return render_template("videos/list.html", videos=Video.query.all())


@bp.route('/')
def index():
    return render_template("index.html")
