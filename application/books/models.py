from application import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    author = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(400), nullable=False)
    category = db.Column(db.String(144), nullable=False)

    def __init__(self, name, author, description):
        self.name = name
        self.author = author
        self.description = description
