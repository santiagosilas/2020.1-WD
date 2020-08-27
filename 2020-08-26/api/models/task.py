from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from api import db, ma

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    date = db.Column(db.DateTime)

    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.date = datetime.now()

class TaskSchema(ma.Schema):
    class Meta:
        model = Task
        fields = ("id", "title", "date")