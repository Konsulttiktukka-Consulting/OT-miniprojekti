from application import db


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(144), nullable=False)
    url = db.Column(db.String(144), nullable=False)
    category = db.Column(db.String(400), nullable=False)

    def __init__(self, title, url):
        self.title = title
        self.url = url
        self.category = 'Video'
