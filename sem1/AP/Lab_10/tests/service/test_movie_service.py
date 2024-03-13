import os
import shutil
from unittest import TestCase

from ro.ubb.store.domain.movie import Movie
from ro.ubb.store.repository.file_repository import FileRepository
from ro.ubb.store.service.movie_service import MovieService


class TestMovieService(TestCase):
    def setUp(self) -> None:
        self.file_repository = FileRepository('test_file_repo')
        self.movie_service = MovieService(self.file_repository)
        shutil.rmtree('repository/text_files', ignore_errors=True)
        os.makedirs('repository/text_files')
        with open('repository/text_files/test_file_repo', 'w') as file:
            file.write('1 Title_1 Description_1 Genre_1\n')
            file.write('2 Title_2 Description_2 Genre_2\n')

    def test_create_movie(self):
        movie = self.movie_service.add_movie(1, 'test1', 'test2', 'test3')
        self.assertTrue(isinstance(movie, Movie), 'Instanta trebuie sa fie Movie')
        self.assertTrue(movie.id == 1, 'ID film trebuie sa fie 1')
        self.assertTrue(movie.title == 'test1', 'Titlu film trebuie sa fie test1')
        self.assertTrue(movie.description == 'test2', 'Descriere film trebuie sa fie test2')
        self.assertTrue(movie.genre == 'test3', 'Gen film trebuie sa fie test3')

    def test_load_from_file(self):
        self.movie_service.load_from_file()
        self.assertTrue(len(self.movie_service.get_all_entities()) == 2)

    def tearDown(self) -> None:
        shutil.rmtree('repository/text_files')
