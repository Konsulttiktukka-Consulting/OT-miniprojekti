from application import db

class Podcast(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    author = db.Column(db.String(144), nullable=False)
    title = db.Column(db.String(144), nullable=False)
    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(400), nullable=False)
    category = db.Column(db.String(144), nullable=False)

    def __init__(self, author, title, name, description):
        self.author = author
        self.title = title
        self.name = name
        self.description = description
        self.category = 'Podcast'
