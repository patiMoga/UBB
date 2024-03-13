import os
import shutil
from unittest import TestCase

from ro.ubb.store.domain.client import Client
from ro.ubb.store.repository.file_repository import FileRepository

from ro.ubb.store.service.service import Service


class TestService(TestCase):
    def setUp(self) -> None:
        self.file_repository = FileRepository('test_file_repo')
        self.service = Service(self.file_repository)
        shutil.rmtree('repository/text_files', ignore_errors=True)
        os.makedirs('repository/text_files')
        with open('repository/text_files/test_file_repo.txt', 'w') as file:
            file.write('3 test3 123\n')
            file.write('4 test4 456\n')

        self.service.add_entity(Client(1, 'test1', 69))
        self.service.add_entity(Client(2, 'test2', 420))

    def test_get_all(self):
        client_list = self.service.get_all_entities()
        self.assertTrue(len(client_list) == 2, 'Length of client list should be 2')

    def test_get_by_id(self):
        client = self.service.entity_byID(1)
        self.assertTrue(client.id == 1, 'Id of client should be 1')
        self.assertTrue(client.name == 'test1', 'Name of client should be test1')
        self.assertTrue(client.CNP == 69, 'Ssn of client should be 69')

    def test_add_entity(self):
        self.service.add_entity(Client(3, 'Phantom', 420))
        client_list = self.service.get_all_entities()
        self.assertTrue(len(client_list) == 3, 'Length of client list should be 3')

    def test_update_entity(self):
        self.service.modify_entity(Client(1, 'Phantom', 420))
        client = self.service.entity_byID(1)
        self.assertTrue(client.id == 1, 'Id of client should be 1')
        self.assertTrue(client.name == 'Phantom', 'Name of client should be test1')
        self.assertTrue(client.CNP == 420, 'Ssn of client should be 69')

    def test_delete_entity(self):
        self.service.delete_entity(1)
        client_list = self.service.get_all_entities()
        self.assertTrue(len(client_list) == 1, 'Length of client list should be 1')

    def test_file_get_line(self):
        file_line = self.service.file_get_lines()
        self.assertTrue(len(file_line) == 2)

    def test_file_delete(self):
        self.service.file_delete_contents()
        file_list = self.service.file_get_lines()
        self.assertTrue(len(file_list) == 0)


    def tearDown(self) -> None:
        pass
