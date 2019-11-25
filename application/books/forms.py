from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators


class BookForm(FlaskForm):
    name = StringField(
        "Book title", [validators.DataRequired(), validators.Length(min=2)])
    author = StringField(
        "Book author", [validators.DataRequired(), validators.Length(min=2)])
    description = TextAreaField("Description", [validators.DataRequired()])

    class Meta:
        csrf = False
