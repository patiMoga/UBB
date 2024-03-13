import os
import shutil
from unittest import TestCase

from ro.ubb.store.domain.client import Client
from ro.ubb.store.domain.rent import Rent
from ro.ubb.store.repository.file_repository import FileRepository
from ro.ubb.store.repository.repository import GenericRepository
from ro.ubb.store.service.rent_service import RentService


class TestRentService(TestCase):
    def setUp(self) -> None:

        self.generic_repository = FileRepository('test_file_repo')
        self.client_repository = GenericRepository()
        self.rent_repository = GenericRepository()
        self.__rent_service = RentService(self.generic_repository, self.client_repository)

        self.file_repository = FileRepository('test_file_repo')
        self.file_client_service = RentService(self.file_repository, self.client_repository)
        shutil.rmtree('repository/text_files', ignore_errors=True)
        os.makedirs('repository/text_files')

        self.client_repository.add_entity(Client(1, 'test1', 123))
        self.client_repository.add_entity(Client(2, 'test2', 234))

        self.__rent_service.add_entity(Rent(1, 1, 1, "17/03/2023", "19/03/2023", "NO"))
        self.__rent_service.add_entity(Rent(2, 2, 1, "19/03/2023", "22/03/2023", "NO"))
        self.__rent_service.add_entity(Rent(3, 2, 2, "16/11/2022", "18/11/2022", "NO"))


        with open('repository/text_files/test_file_repo', 'w') as file:
            file.write('4 1 3 17/03/2023 19/03/2023 NO\n')
            file.write('5 2 3 17/03/2023 19/03/2023 NO\n')


    def test_create_rent(self):
        rent = RentService.add_rent(1, 2, 3, '17/03/2023', '19/03/2023', 'NO')
        self.assertTrue(isinstance(rent, Rent), 'Instanta trebuie sa fie Rent')
        self.assertTrue(rent.id == 1, 'ID rent trebuie sa fie 1')
        self.assertTrue(rent.idMovie == 2, 'ID film trebuie sa fie 2')
        self.assertTrue(rent.idClient == 3, 'ID client trebuie sa fie 3')
        self.assertTrue(rent.beginDate == "17/03/2023", 'Data inceput trebuie sa fie 17/03/2023')
        self.assertTrue(rent.endDate == "19/03/2023", 'Data sfarsit trebuie sa fie 19/03/2023')
        self.assertTrue(rent.returnedRent == 'NO', 'Return trebuie sa fie NO')

    def test_load_from_file(self):
        self.file_client_service.load_from_file()
        self.assertTrue(len(self.file_client_service.get_all_entities()) == 2)

    def test_get_movie_frequency(self):
        frequency = self.__rent_service.get_movie_frequency()
        self.assertTrue(frequency[1] == 1, 'Frecventa de 1 trebuie sa fie 2')
        self.assertTrue(frequency[2] == 2, 'Frecventa de 2 trebuie sa fie 1')

    def test_get_max_movie(self):
        max_movie = self.__rent_service.get_max_movie()
        self.assertTrue(len(max_movie) == 1, 'Lungimea lui max_movie trebuie sa fie 1')
        self.assertTrue(max_movie[0] == 2, 'max_movie = 1 entitate')

        self.__rent_service.add_entity(Rent(6, 3, 3, "19/03/2023", "22/03/2023", "NO"))
        self.__rent_service.add_entity(Rent(7, 3, 2, "16/11/2022", "18/11/2022", "NO"))

        max_movie = self.__rent_service.get_max_movie()
        self.assertTrue(len(max_movie) == 2)
        self.assertTrue(max_movie[0] == 2)
        self.assertTrue(max_movie[1] == 3)

    def test_get_client_frequency(self):
        frequency = self.__rent_service.get_client_frequency()
        self.assertTrue(len(frequency) == 2, 'Lungimea secventei trebuie sa fie 2')
        self.assertTrue(frequency[1] == 2, 'Frecventa de 1 trebuie sa fie 1')
        self.assertTrue(frequency[2] == 1, 'Frecventa de 2 trebuie sa fie 2')

    def test_get_client_names(self):
        client_list = self.__rent_service.get_client_names()
        self.assertTrue(len(client_list) == 2)
        self.assertTrue(client_list[0].name == 'test1')
        self.assertTrue(client_list[0].id == 1)
        self.assertTrue(client_list[1].name == 'test2')
        self.assertTrue(client_list[1].id == 2)

    def test_sort_clients_by_name(self):
        client_list = self.__rent_service.sort_clients_by_name()
        self.assertTrue(len(client_list) == 2)
        self.assertTrue(client_list[0].name == 'test1')
        self.assertTrue(client_list[0].id == 1)
        self.assertTrue(client_list[1].name == 'test2')
        self.assertTrue(client_list[1].id == 2)

    def test_sort_clients_by_frequency(self):
        client_list = self.__rent_service.sort_clients_by_frequency()
        self.assertTrue(len(client_list) == 2)
        self.assertTrue(client_list[0][0] == 1)
        self.assertTrue(client_list[0][1] == 2)
        self.assertTrue(client_list[1][0] == 2)
        self.assertTrue(client_list[1][1] == 1)

    def test_most_active_clients(self):
        client_list = self.__rent_service.most_active_clients()
        self.assertTrue(len(client_list) == 2)
        self.assertTrue(client_list[0].name == "test1")
        self.assertTrue(client_list[0].freq == 2)
        self.assertTrue(client_list[1].name == "test2")
        self.assertTrue(client_list[1].freq == 1)

    def tearDown(self) -> None:
        shutil.rmtree('repository/text_files')
