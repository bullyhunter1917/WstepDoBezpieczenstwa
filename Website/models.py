from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Transfer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(26))
    name = db.Column(db.String(1000))
    surname = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    transfers = db.relationship('Transfer')