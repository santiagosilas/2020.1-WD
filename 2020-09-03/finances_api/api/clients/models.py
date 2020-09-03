from datetime import datetime
from flask_sqlalchemy import SQLAlchemy, declarative_base
#from api.finances import models as finance_models
#from api.finances.models import Record
from api import db, ma

# Tabela de associação
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# Uma coluna representando o relacionamento entre usuários e grupos (muitos para muitos)
clients_groups = db.Table(
    'clients_groups',
    db.Column(
        'client_id', db.Integer, 
        db.ForeignKey('client.id'), primary_key=True),
    
    db.Column(
        'group_id', db.Integer, 
        db.ForeignKey('group.id'), primary_key=True)
)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique=True)
    id_phone = db.Column(db.Integer, db.ForeignKey('phone.id'), nullable=True)
    email = db.Column(db.String(50), unique=True)
    created = db.Column(db.DateTime)

    # cria uma propriedade
    # (não faz parte do banco de dados)
    records = db.relationship(
        'Record',
        
        # backref='client': um jeito simples de declarar também uma nova propriedade na classe Record
        # haverá a propriedade record.client para Record
        backref='client',
        
        # Indica quando os dados serão carregados do banco de dados
        # o	lazy='dynamic' retorna um objeto query que pode ser refinado antes de carregar items.
        lazy='dynamic'  
    )

    # cria uma propriedade que expressa um relacionamento um-para-um (uselist=False)
    phone = db.relationship('Phone',
            backref='client',
            uselist=False)

    groups = db.relationship(
        'Group',
        secondary = clients_groups,
        backref = db.backref('members', lazy='dynamic')
    )

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.created =  datetime.now()




class Group(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    description = db.Column(db.String(30))

    def __init__(self, description):
        self.description = description


class Phone(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    number = db.Column(db.String(50))

    def __init__(self, number):
        self.number = number