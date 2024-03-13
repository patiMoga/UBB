import os
import shutil
from unittest import TestCase

from ro.ubb.store.domain.client import Client
from ro.ubb.store.exceptions.exceptions import DuplicateIdError, MissingIdError
from ro.ubb.store.repository.file_repository import FileRepository


class TestFileRepository(TestCase):
    def setUp(self) -> None:
        shutil.rmtree('repository/text_files', ignore_errors=True)
        os.makedirs('repository/text_files')
        with open('repository/text_files/test_file_repo', 'w') as file:
            file.write('1 test1 123\n')
            file.write('2 test2 224\n')

        self.file_repository = FileRepository('test_file_repo')

        for entity in self.file_repository.file_read():
            entity = entity.strip()
            entity = entity.split(" ")
            FileRepository.add_entity(self.file_repository, Client(int(entity[0]), entity[1], int(entity[2])))

    def test_add_entity(self):
        with self.assertRaises(DuplicateIdError):
            self.file_repository.add_entity(Client(1, "test2", 224))
        self.file_repository.add_entity(Client(3, 'test3', 120))
        self.assertTrue(len(self.file_repository.print_all()) == 3)

    def test_update_entity(self):
        with self.assertRaises(MissingIdError):
            self.file_repository.modify_entity(Client(4, "test2", 224))
        self.file_repository.modify_entity(Client(1, 'test3', 120))
        self.assertTrue(FileRepository.get_ID(self.file_repository, 1).id == 1)
        self.assertTrue(FileRepository.get_ID(self.file_repository, 1).name == 'test3')
        self.assertTrue(FileRepository.get_ID(self.file_repository, 1).CNP == 120)

    def test_delete_entity(self):
        self.file_repository.delete_entity(1)
        self.assertTrue(len(self.file_repository.print_all()) == 1)
        with self.assertRaises(MissingIdError):
            self.file_repository.delete_entity(3)

    def test_get_file_line_by_id(self):
        self.assertTrue(self.file_repository.get_file_line_by_id(1) == '1 test1 123')

    def test_file_delete_entity(self):
        self.file_repository.file_delete_entity(1)
        self.assertTrue(self.file_repository.get_file_line_by_id(1) is None)
        self.assertTrue(self.file_repository.get_file_line_by_id(2) is not None)

    def test_file_append_entity(self):
        self.file_repository.file_append_entity(Client(3, 'test3', 120))
        self.assertTrue(self.file_repository.get_file_line_by_id(3) == '3 test3 120')

    def test_file_read(self):
        file_list = self.file_repository.file_read()
        self.assertTrue(file_list[0] == '1 test1 123')
        self.assertTrue(file_list[1] == '2 test2 224')

    def test_file_delete(self):
        self.file_repository.file_delete()
        self.assertTrue(self.file_repository.get_file_line_by_id(1) is None)
        self.assertTrue(self.file_repository.get_file_line_by_id(2) is None)

    def tearDown(self) -> None:
        shutil.rmtree('repository/text_files')
