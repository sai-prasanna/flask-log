from app import db
from datetime import datetime
from slugify import slugify

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    slug = db.Column(db.String(255))
    body = db.Column(db.String)
    timestamp = db.Column(db.DateTime)
    comments = db.relationship('Comment', backref='post',
                                lazy='dynamic')

    def __init__(self, title, body):
        self.title = title
        self.slug = slugify(title)
        self.body = body
        self.timestamp = datetime.utcnow()

    def __repr__(self):
        return '<Post %r>' % (self.slug)

    def __unicode__(self):
        return self.title

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(500))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
