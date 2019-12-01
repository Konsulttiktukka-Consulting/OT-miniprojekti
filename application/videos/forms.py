from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators


class VideoForm(FlaskForm):
    title = StringField(
        "Video title", [validators.DataRequired(), validators.Length(min=2)])
    url = StringField(
        "Video URL", [validators.DataRequired(), validators.Length(min=2)])

    class Meta:
        csrf = False
