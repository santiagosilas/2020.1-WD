import sys
from datetime import datetime
sys.path.insert(0, '../')

from api import create_api, db
from api.finances.services import RecordService
from api.clients.services import ClientService
from api.finances.models import Record
from api.clients.models import Client, Phone

# cria o objeto flask
current_api = create_api('config')

with current_api.app_context():

    # remove todas as tabelas do banco
    db.drop_all()

    # (re)cria o banco de dados
    db.create_all()

    # obter os registros na base de dados
    records = RecordService.get_all()
    print(f'records {list(records)}')

    # cria um usuário e o adiciona ao banco
    client_1 = ClientService.add('admin', 'admin@finances.org')
    print(client_1)

    client_2 = ClientService.add('admin1', 'admin1@finances.org')
    print(client_1)

    client_3 = ClientService.add('admin2', 'admin2@finances.org')
    print(client_1)

    client_4 = ClientService.add('admin3', 'admin3@finances.org')
    print(client_1)

    # cria um registro
    r = RecordService.add(id_client = client_1.id, descr='any', amount=8.57, dt=datetime.now())
    r = RecordService.add(id_client = client_1.id, descr='any', amount=18.57, dt=datetime.now())
    r = RecordService.add(id_client = client_1.id, descr='any', amount=18.17, dt=datetime.now())
    r = RecordService.add(id_client = client_1.id, descr='any', amount=5.57, dt=datetime.now())
    r = RecordService.add(id_client = client_1.id, descr='any', amount=2.57, dt=datetime.now())
    print(r)


    # Filtrando resultados por titulo
    records = Record.query.filter_by(id_client = client_1.id).all()
    print(records)
    print(records[0].description)

    # Obtém todas os registros, ordenados por descrição
    records = Record.query.order_by(Record.description)

    # Obtendo um registro a partir de sua chave primária
    r = Record.query.get(1)
    if r is not None:
        print('busca', r.description)
    else:
        print('registro não existente.')

    # update
    r.description = 'nothing'
    db.session.commit()

    # update
    client_1.phone  = Phone('04185 3421-1234')
    db.session.commit()

    # Remove um registro
    r = Record.query.all()[0]
    db.session.delete(r)
    db.session.commit()

    # acesso via propriedades
    print(r.client)
    print(r.client.id)
    print(r.client.username)
    print(r.client.email)
    print(r.client.phone.number)

    # acesso via propriedades
    print(client_1.records.all())

    # exibe o registro adicionado