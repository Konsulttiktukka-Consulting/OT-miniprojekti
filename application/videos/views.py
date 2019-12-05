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
DEVELOPER_KEY = os.getenv("API_KEY")
if os.environ.get("HEROKU", 2) == 1:
    DEVELOPER_KEY = os.environ.get("API_KEY")

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
            if "youtu" in form.url.data:
                try:
                    api_service_name = "youtube"
                    api_version = "v3"

                    youtube = googleapiclient.discovery.build(
                        api_service_name, api_version, developerKey=DEVELOPER_KEY)

                    if "?v=" in form.url.data:
                        video_id = re.search(r'(?<=\?v=).{11}',form.url.data)[0]
                    else:
                        video_id = re.search(r'(?<=\.be\/).{11}',form.url.data)[0]

                    res = youtube.videos().list(
                        part="snippet",
                        id=video_id
                    )
                    response = res.execute()
                    data = response["items"][0]

                    url = data["id"]
                    title = data["snippet"]["title"]
                    description = data["snippet"]["description"][:150]
                    creator = data["snippet"]["channelTitle"]
                    platform = "youtube"
                    new_video = Video(title, url, creator, description, platform)
                    db.session().add(new_video)
                    db.session.commit()

                    return redirect(url_for("videos.videos_index"))
                except:
                    form.url.errors = [
                        f"Wrong url, url must be typed like 'https://www.youtube.com/watch?v=StqIbgNA35s'"]
                    return render_template("videos/new.html", form=form)
            elif "twitch" in form.url.data:
                url = form.url.data
                title = re.search(r'(?<=.tv\/).*',url)[0]
                description = "none"
                creator = title
                platform = "twitch"
                new_video = Video(title, url, creator, description, platform)
                db.session().add(new_video)
                db.session.commit()
                return redirect(url_for("videos.videos_index"))


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
