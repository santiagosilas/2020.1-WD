
import unittest

import sys
from datetime import datetime
sys.path.insert(0, '../')

from api import create_api, db
from api.clients.services import ClientService

class TestRecommender(unittest.TestCase):
    def setUp(self):
        # cria o objeto flask
        self.current_api = create_api('config')
        with self.current_api.app_context():

            # remove todas as tabelas do banco
            db.drop_all()

            # (re)cria o banco de dados
            db.create_all()
            

    def test_add(self):
        with self.current_api.app_context():
            client = ClientService.add('admin', 'admin@finances.org')
            self.assertNotEqual(client.id, None)

    def test_get_all(self):
        with self.current_api.app_context():
            ClientService.add('admin1', 'admin1@finances.org')
            ClientService.add('admin2', 'admin2@finances.org')
            ClientService.add('admin3', 'admin3@finances.org')
            clients = ClientService.get_all()
            self.assertNotEqual(len(clients), 0)

    def test_get_by_username(self):
        with self.current_api.app_context():
            ClientService.add('admin1', 'admin1@finances.org')
            client = ClientService.get_by_username('admin1')
            self.assertNotEqual(client, 0)

    def test_get_by_email(self):
        with self.current_api.app_context():
            ClientService.add('admin1', 'admin1@finances.org')
            client = ClientService.get_by_email('admin1@finances.org')
            self.assertNotEqual(client, None)

    def test_update(self):
        with self.current_api.app_context():
            ClientService.add('admin1', 'admin1@finances.org')
            client = ClientService.get_by_email('admin1@finances.org')
            
            updated_client = ClientService.update(client.id, 'admin42', 'admin42@gmail.com')
            self.assertEqual(updated_client.id, client.id)

            updated_client = ClientService.update(
                987, 'admin42', 'admin42@gmail.com')
            self.assertEqual(updated_client, None)

    def test_update_username(self):
        with self.current_api.app_context():
            ClientService.add('admin1', 'admin1@finances.org')
            client = ClientService.get_by_email('admin1@finances.org')
            
            updated_client = ClientService.update_username(
                client.id, 'admin42')
            self.assertEqual(updated_client.id, client.id)

            updated_client = ClientService.update_username(
                987, 'admin42')
            self.assertEqual(updated_client, None)

    def test_update_email(self):
        with self.current_api.app_context():
            ClientService.add('admin1', 'admin1@finances.org')
            client = ClientService.get_by_email('admin1@finances.org')
            
            updated_client = ClientService.update_email(
                client.id, 'admin42')
            self.assertEqual(updated_client.id, client.id)

            updated_client = ClientService.update_email(
                987, 'admin42')
            self.assertEqual(updated_client, None)

    def test_remove(self):
        with self.current_api.app_context():
            ClientService.add('admin1', 'admin1@finances.org')
            client = ClientService.get_by_email('admin1@finances.org')
            
            deleted_client = ClientService.remove(
                client.id)
            self.assertEqual(deleted_client.id, client.id)

            deleted_client = ClientService.remove(
                987)
            self.assertEqual(deleted_client, None)

if __name__ == '__main__':
    unittest.main()




