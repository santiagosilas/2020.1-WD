from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from api.clients.models import Client
from api import db, ma

class Record(db.Model):

    # chave primária
    id = db.Column(db.Integer, primary_key = True)

    # um registro pertence a um usuario
    id_client = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)  

    # descrição
    description = db.Column(db.String(20))

    # valor
    amount = db.Column(db.Float)

    # Data/Hora
    dt = db.Column(db.DateTime, nullable=False)

    # construtor
    def __init__(self, id_client, descr, amount, dt):
        self.id_client = id_client
        self.description = descr
        self.amount = amount
        self.dt = dt

class RecordSchema(ma.Schema):
    class Meta:
        model = Record
        fields = ('id', )