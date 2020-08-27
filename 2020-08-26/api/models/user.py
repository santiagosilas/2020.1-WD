from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from api import db, ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    created = db.Column(db.DateTime)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.created =  datetime.now()

class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')