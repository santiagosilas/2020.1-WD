from api import app, db
from api.models import task

def drop_db():
    db.drop_all()

def create_db():
    db.create_all(app=app)
    print("Banco criado.")

def populate_db():
    pass