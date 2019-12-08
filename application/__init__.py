import os

import click
from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    db_url = os.environ.get("DATABASE_URL")

    if db_url is None:
        db_url = "sqlite:///" + \
            os.path.join(app.instance_path, "application.sqlite")
        os.makedirs(app.instance_path, exist_ok=True)

    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev"),
        SQLALCHEMY_DATABASE_URI=db_url,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)

    db.init_app(app)
    app.cli.add_command(init_db_command)

    # apply the blueprints to the app
    from application import videos

    app.register_blueprint(videos.bp)

    app.add_url_rule("/", endpoint="index")

    return app


def init_db():
    from application.videos.models import Video

    db.drop_all()
    db.create_all()
    initial_video = Video("Iha ok mut ootko kattonu simpsonit sarjasta jakson himo läski homer", "QyYyuTsx9lE", "Goolag User",
                          "iha ok mut ootko kattonu simpsonit sarjasta jakson himo läski homer :D siinä esiintyy koko simpsonit perhe",
                          "youtube")
    initial_stream = Video("DreamHackCS",
                           "https://www.twitch.tv/dreamhackcs",
                           "DreamHackCS","DreamHack's Counter-Strike: Global Offensive channel.",
                           "twitch")

    db.session().add(initial_video)
    db.session().add(initial_stream)
    db.session().commit()


def init_test_db():
    db.drop_all()
    db.create_all()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


app = create_app()
