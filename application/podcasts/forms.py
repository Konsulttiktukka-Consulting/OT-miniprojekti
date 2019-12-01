from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class PodcastForm(FlaskForm):
    author = StringField(
        "Podcast author", [validators.DataRequired(), validators.Length(min=2)])
    title = StringField(
        "Podcast title", [validators.DataRequired(), validators.Length(min=2)])
    name = StringField(
        "Podcast name", [validators.DataRequired(), validators.Length(min=2)])
    description = TextAreaField(
        "Podcast description", [validators.DataRequired(), validators.Length(min=2)])

    class Meta:
        csrf = False
