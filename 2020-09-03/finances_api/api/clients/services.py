from api import db, ma
from api.clients.models import Client
from api.clients.schemas import ClientSchema

class ClientService:
    @staticmethod
    def get_all():
        clients = Client.query.all()
        return clients

    @staticmethod
    def get_by_id(client_id):
        client = Client.query.get(client_id)  
        return client

    @staticmethod
    def add(username, email):
        client = Client(username, email)
        db.session.add(client)
        db.session.commit()
        return client

    @staticmethod
    def get_by_username(username):
        clients = Client.query.filter_by(
            username = username).all()
        if len(clients) > 0:
            return clients[0]
        else:
            return None
    
    @staticmethod
    def get_by_email(email):
        client = Client.query.filter_by(
            email = email).first()
        return client

    @staticmethod
    def update(client_id, username, email):
        client = Client.query.get(client_id)
        if client is not None:
            client.username = username
            client.email = email 
            db.session.commit()  
        return client

    @staticmethod
    def update_username(client_id, username):
        client = Client.query.get(client_id)
        if client is not None:
            client.username = username  
            db.session.commit()
        return client

    @staticmethod
    def update_email(client_id, email):
        client = Client.query.get(client_id)
        if client is not None:
            client.email = email 
            db.session.commit()  
        return client

    @staticmethod
    def remove(client_id):
        client = Client.query.get(client_id)
        if client is not None:
            db.session.delete(client)
            db.session.commit()  
        return client

    @staticmethod
    def paginate(per_page, page):
        clients = Client.query.paginate(
            per_page = per_page, page = page)
        return clients