import sys
from datetime import datetime
sys.path.insert(0, '../')

from api import create_api, db
from api.clients.models import Client
from api.clients.services import ClientService
from api.finances.services import RecordService

api = create_api('config')

if __name__ == "__main__":
    with api.app_context():

        # remove todas as tabelas do banco
        db.drop_all()

        # (re)cria o banco de dados
        db.create_all()

        # Testes de consultas
        users = Client.query.all()

        # Adiciona um usuário
        username, email = 'admin', 'admin@finances.com'
        u = Client(username, email)
        db.session.add(u)
        db.session.commit()

        data = ClientService.get_all()
        print(data)

        data = RecordService.get_all()
        print(data)