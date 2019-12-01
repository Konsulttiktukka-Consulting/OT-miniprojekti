from application import db


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(144), nullable=False)
    url = db.Column(db.String(400), nullable=False)
    author = db.Column(db.String(144), nullable=True)
    description = db.Column(db.String(400), nullable=True)
    category = db.Column(db.String(144), nullable=False)

    def __init__(self, title, url, author, description):
        self.title = title
        self.url = url  
        self.author = author
        self.description = description
        self.category = 'BlogPost'