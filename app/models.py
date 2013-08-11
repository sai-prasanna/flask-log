from app import db
import datetime
from flask import url_for

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    body = db.Column(db.String)
    timestamp = db.Column(db.DateTime)

    def __unicode__(self):
        return self.title



    
