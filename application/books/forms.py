from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class BookForm(FlaskForm):
    name = StringField("Book title", [validators.DataRequired()])
    author = StringField("Book author", [validators.DataRequired()])
    description = TextAreaField("Description", [validators.DataRequired()])

    class Meta:
        csrf = False

