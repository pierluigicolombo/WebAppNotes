from datetime import timezone
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    '''
    model for the Note Object
    '''
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(100000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    '''
    model for the User Object. inheritance from db.Model and UserMixin (for login)
    '''
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')