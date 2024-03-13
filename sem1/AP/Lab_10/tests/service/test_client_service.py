import os
import shutil
from unittest import TestCase

from ro.ubb.store.domain.client import Client
from ro.ubb.store.repository.file_repository import FileRepository
from ro.ubb.store.service.client_service import ClientService


class TestClient(TestCase):
    def setUp(self) -> None:
        self.file_repository = FileRepository('test_file_repo.txt')
        self.client_service = ClientService(self.file_repository)
        shutil.rmtree('repository/text_files', ignore_errors=True)
        os.makedirs('repository/text_files')
        with open('repository/text_files/test_file_repo.txt', 'w') as file:
            file.write('1 test1 123\n')
            file.write('2 test2 456\n')

    def test_create_client(self):
        client = ClientService.add_client(1, 'test', 123)
        self.assertTrue(isinstance(client, Client), 'Instanta trebuie sa fie Client')
        self.assertTrue(client.id == 1, 'ID client trebuie sa fie 1')
        self.assertTrue(client.name == 'test', 'Numele client trebuie sa fie test')
        self.assertTrue(client.CNP == 123, 'CNP client trebuie sa fie 123')

    def test_load_from_file(self):
        self.client_service.load_from_file()
        self.assertTrue(len(self.client_service.get_all_entities()) == 2)

    def tearDown(self) -> None:
        shutil.rmtree('repository/text_files')
