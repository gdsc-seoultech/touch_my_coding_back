import uuid
from database import db

class Test(db.Model):

    __tablename__ = "tests"

    id = db.Column(db.Integer, primary_key = True, nullable=False)
    name = db.Column(db.String(20, 'utf8mb4_unicode_ci'))
    email = db.Column(db.String(50, 'utf8mb4_unicode_ci'))

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
