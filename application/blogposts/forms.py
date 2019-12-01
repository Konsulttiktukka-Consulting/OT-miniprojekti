from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators


class BlogPostForm(FlaskForm):
    title = StringField(
        "Blog Post title", [validators.DataRequired(), validators.Length(min=2)])
    url = StringField(
        "Blog post url", [validators.DataRequired(), validators.Length(min=2)])
    #description = TextAreaField("Description", [validators.DataRequired()])

    class Meta:
        csrf = False
