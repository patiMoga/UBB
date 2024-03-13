from unittest import TestCase

from ro.ubb.store.domain.movie import Movie


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie(1, "title1", "description1", "genre1")

    def test_id(self):
        self.assertTrue(self.movie.id == 1)
        self.assertFalse(self.movie.id == 'a', "ID film nu trebuie sa fie a")

    def test_title(self):
        self.assertTrue(self.movie.title == 'title1', "Titlu film trebuie sa fie test1")
        self.assertFalse(self.movie.title == 123, "Titlu film nu trebuie sa fie 123")

    def test_description(self):
        self.assertTrue(self.movie.description == 'description1', "Descriere film trebuie sa fie description1")
        self.assertFalse(self.movie.description == 456, "Descriere film nu trebuie sa fie 456")

    def test_genre(self):
        self.assertTrue(self.movie.genre == 'genre1', "Gen film trebuie sa fie genre1")
        self.assertFalse(self.movie.genre == 789, "Gen film nu trebuie sa fie 789")

    def test_id_set(self):
        self.movie.id = 2
        self.assertTrue(self.movie.id == 2, "ID film trebuie sa fie 2")
        self.assertFalse(self.movie.id == 1, "ID film nu trebuie sa fie 1")

    def test_title_set(self):
        self.movie.title = 'title2'
        self.assertTrue(self.movie.title == 'title2', "Titlu film trebuie sa fie title2")
        self.assertFalse(self.movie.title == 'title1', "Titlu film nu trebuie sa fie title1")

    def test_description_set(self):
        self.movie.description = 'description2'
        self.assertTrue(self.movie.description == 'description2', "Descriere film trebuie sa fie description2")
        self.assertFalse(self.movie.description == 'description1', "Descriere film nu trebuie sa fie description1")

    def test_genre_set(self):
        self.movie.genre = 'genre2'
        self.assertTrue(self.movie.genre == 'genre2', "Gen film trebuie sa fie genre2")
        self.assertFalse(self.movie.genre == 'genre1', "Gen film nu trebuie sa fie genre1")

    def test_movie_str(self):
        self.assertTrue(self.movie.__str__() == '1 title1 description1 genre1',
                        "Date film trebuie sa fie '1 title1 description1 genre1'")
        self.assertFalse(self.movie.__str__() == 'a 123 456 789',
                         "Date film nu trebuie sa fie 'a 123 456 789'")

    def tearDown(self) -> None:
        pass
