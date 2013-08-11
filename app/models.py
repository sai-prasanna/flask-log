from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    slug = db.Column(db.String(255), unique=True)
    body = db.Column(db.String)
    timestamp = db.Column(db.DateTime)

    def __unicode__(self):
        return self.title
