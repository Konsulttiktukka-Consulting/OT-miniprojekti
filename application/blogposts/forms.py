from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators


class BlogPostForm(FlaskForm):
    author = StringField("Blog Post author")
    title = StringField(
        "Blog Post title", [validators.DataRequired(), validators.Length(min=2)])
    url = StringField(
        "Blog post url", [validators.DataRequired(), validators.Length(min=2)])
    description = TextAreaField("Description")

    class Meta:
        csrf = False
