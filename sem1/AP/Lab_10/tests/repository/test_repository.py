from unittest import TestCase

from ro.ubb.store.domain.client import Client
from ro.ubb.store.domain.movie import Movie
from ro.ubb.store.domain.rent import Rent
from ro.ubb.store.exceptions.exceptions import DuplicateIdError, MissingIdError
from ro.ubb.store.repository.repository import GenericRepository


class TestRepository(TestCase):
    def setUp(self):
        self.client_repository = GenericRepository()
        self.movie_repository = GenericRepository()
        self.rent_repository = GenericRepository()
        self.client_repository.add_entity(Client(1, 'nume_1', 123))
        self.client_repository.add_entity(Client(2, 'nume_2', 202))
        self.movie_repository.add_entity(Movie(1, 'movie_1', 'yes', 'no'))
        self.movie_repository.add_entity(Movie(2, 'movie_2', 'yes', 'no'))
        self.rent_repository.add_entity(Rent(1, 1, 1, '17/03/2023', "19/03/2023", "NO"))
        self.rent_repository.add_entity(Rent(2, 2, 2, '17/03/2023', "19/03/2023", "NO"))

    def test_get_clients(self):
        client_list = self.client_repository.print_all()
        self.assertTrue(len(client_list) == 2, 'Lungime listei trebuie sa fie 2')

    def test_get_movies(self):
        movie_list = self.movie_repository.print_all()
        self.assertTrue(len(movie_list) == 2, 'Lungime listei trebuie sa fie 2')

    def test_get_rents(self):
        rent_list = self.rent_repository.print_all()
        self.assertTrue(len(rent_list) == 2, 'Lungime listei trebuie sa fie 2')

    def test_get_ID_client(self):
        client = self.client_repository.get_ID(2)
        self.assertTrue(client.id == 2, 'ID = 2')
        self.assertTrue(client.name == 'nume_2', 'nume = nume_2')
        self.assertTrue(client.CNP == 202, 'CNP = 202')

    def test_get_ID_movie(self):
        movie = self.movie_repository.get_ID(2)
        self.assertTrue(movie.id == 2, 'ID = 2')
        self.assertTrue(movie.title == 'movie_2', 'Titlu = movie_2')
        self.assertTrue(movie.description == 'yes', "Descr = yes")
        self.assertTrue(movie.genre == 'no', 'Gen = no')

    def test_get_ID_rent(self):
        rent = self.rent_repository.get_ID(1)
        self.assertTrue(rent.id == 1, 'ID = 1')
        self.assertTrue(rent.idMovie == 1, 'ID film = 1')
        self.assertTrue(rent.idClient == 1, 'ID client = 1')
        self.assertTrue(rent.beginDate == '17/03/2023', 'Data de inceput = 17/03/2023')
        self.assertTrue(rent.endDate == '19/03/2023', 'Data de sfarsit = 19/03/2023')
        self.assertTrue(rent.returnedRent == 'NO', 'Returnat = NO')

    def test_add_client(self):
        self.client_repository.add_entity(Client(3, 'nume_3', 420))
        client_list = self.client_repository.print_all()
        self.assertTrue(len(client_list) == 3, 'Lungime lista = 3')
        with self.assertRaises(DuplicateIdError):
            self.client_repository.add_entity(Client(3, 'nume_3', 420))

    def test_add_movie(self):
        self.movie_repository.add_entity(Movie(3, 'movie_3', 'yes', 'no'))
        movie_list = self.movie_repository.print_all()
        self.assertTrue(len(movie_list) == 3, 'Lungime lista = 3')
        with self.assertRaises(DuplicateIdError):
            self.movie_repository.add_entity(Movie(3, 'movie_3', 'yes', 'no'))

    def test_add_rent(self):
        self.rent_repository.add_entity(Rent(3, 1, 2, '17/03/2023', '19/03/2023', 'yes'))
        rent_list = self.rent_repository.print_all()
        self.assertTrue(len(rent_list) == 3, 'Lungime lista = 3')
        with self.assertRaises(DuplicateIdError):
            self.rent_repository.add_entity(Rent(3, 2, 2, '17/03/2023', '19/03/2023', 'no'))

    def test_update_client(self):
        self.client_repository.modify_entity(Client(1, 'client_new', 420))
        client = self.client_repository.get_ID(1)
        self.assertTrue(client.id == 1, 'ID client = 1')
        self.assertTrue(client.name == 'client_new', 'Nume client = client_new')
        self.assertTrue(client.CNP == 420, 'CNP client = 420')
        with self.assertRaises(MissingIdError):
            self.assertTrue(self.client_repository.modify_entity(Client(5, 'client', 420)) is None)

    def test_update_movie(self):
        self.movie_repository.modify_entity(Movie(1, 'movie_new', 'asd', 'asd'))
        movie = self.movie_repository.get_ID(1)
        self.assertTrue(movie.id == 1, 'ID film = 1')
        self.assertTrue(movie.title == 'movie_new', 'Nume film = movie_new')
        self.assertTrue(movie.description == 'asd', 'Descriere film = asd')
        self.assertTrue(movie.genre == 'asd', 'Gen film = asd')
        with self.assertRaises(MissingIdError):
            self.assertTrue(self.movie_repository.modify_entity(Movie(5, 'movie', 'asd', 'asd')) is None)

    def test_update_rent(self):
        self.rent_repository.modify_entity(Rent(1, 2, 2, '19/03/2023', '22/03/2023', 'YES'))
        rent = self.rent_repository.get_ID(1)
        self.assertTrue(rent.id == 1)
        self.assertTrue(rent.idMovie == 2)
        self.assertTrue(rent.idClient == 2)
        self.assertTrue(rent.beginDate == '19/03/2023')
        self.assertTrue(rent.endDate == '22/03/2023')
        self.assertTrue(rent.returnedRent == 'YES')
        with self.assertRaises(MissingIdError):
            self.assertTrue(self.rent_repository.modify_entity(Rent(5, 6, 6, ' ', ' ', ' ')))

    def test_delete_client(self):
        self.client_repository.delete_entity(1)
        client_list = self.client_repository.print_all()
        self.assertTrue(len(client_list) == 1, 'Length of client list should be 1')
        with self.assertRaises(MissingIdError):
            self.assertTrue(self.client_repository.delete_entity(5) is None)

    def test_delete_movie(self):
        self.movie_repository.delete_entity(1)
        movie_list = self.movie_repository.print_all()
        self.assertTrue(len(movie_list) == 1)
        with self.assertRaises(MissingIdError):
            self.assertTrue(self.client_repository.delete_entity(5) is None)

    def test_delete_rent(self):
        self.rent_repository.delete_entity(1)
        rent_list = self.rent_repository.print_all()
        self.assertTrue(len(rent_list) == 1)
        with self.assertRaises(MissingIdError):
            self.assertTrue(self.rent_repository.delete_entity(5) is None)

    def test_get_entities(self):
        self.assertTrue(len(list(self.movie_repository.get_entities())) == 2)
        self.assertTrue(len(list(self.client_repository.get_entities())) == 2)
        self.assertTrue(len(list(self.rent_repository.get_entities())) == 2)

    def tearDown(self) -> None:
        pass
