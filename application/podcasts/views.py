from flask import Blueprint, flash, g, redirect, render_template, request, url_for

from application import db
from application.podcasts.models import Podcast
from application.podcasts.forms import PodcastForm

bp = Blueprint("podcasts", __name__)

@bp.route("/podcasts/new/")
def podcasts_form():
    form = PodcastForm()
    return render_template("podcasts/new.html", form=form)

@bp.route("/podcasts/", methods=["GET", "POST"])
def podcasts_create():
    form = PodcastForm(request.form)
    if form.validate_on_submit():
        new_podcast = Podcast(form.author.data, form.title.data, form.name.data, form.description.data)
        db.session().add(new_podcast)
        db.session().commit()
        return redirect(url_for("books.books_index"))

    return render_template("podcasts/new.html", form=form)

@bp.route("/podcasts/update/<podcast_id>/", methods=["GET", "POST"])
def podcasts_update(podcast_id):
    podcast = Podcast.query.get(podcast_id)
    form = PodcastForm()
    if form.validate_on_submit():
        form.populate_obj(podcast)
        db.session().commit()
        return redirect(url_for("books.books_index"))

    form = PodcastForm(obj=podcast)
    return render_template("podcasts/update.html", podcast=podcast, form=form)

@bp.route("/podcasts/<podcast_id>", methods=["GET", "POST"])
def podcasts_show(podcast_id):
    podcast = Podcast.query.get(podcast_id)
    return render_template("podcasts/podcast.html", podcast=podcast)
