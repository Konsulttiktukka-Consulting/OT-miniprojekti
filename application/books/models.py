from application import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(144), nullable=False)
    author = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(400), nullable=False)
    category = db.Column(db.String(144), nullable=False)

    def __init__(self, title, author, description):
        self.title = title
        self.author = author
        self.description = description
        self.category = 'Book'
