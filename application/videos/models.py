from application import db

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(144), nullable=False)
    url = db.Column(db.String(144), nullable=False)
    creator = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    platform = db.Column(db.String(144), nullable=False)

    def __init__(self, title, url, creator, description, platform):
        self.title = title
        self.url = url
        self.title = title
        self.creator = creator
        self.platform = platform
        self.description = description
