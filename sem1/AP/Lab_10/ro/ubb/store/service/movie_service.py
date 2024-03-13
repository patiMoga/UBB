from ro.ubb.store.domain.movie import Movie
from ro.ubb.store.exceptions.exceptions import Validators
from ro.ubb.store.service.service import Service


class MovieService(Service):

    @staticmethod
    def add_movie(idMovie, title, description, genre):
        """
        Functia returnează entitatea cu datele introduse in UI
        :param idMovie: int
        :param title: str
        :param description: str
        :param genre: str
        :return: entity
        """
        Validators.validate_movie(idMovie, title, description, genre)
        return Movie(idMovie, title, description, genre)


    def load_from_file(self):
        """
        Functia adauga entitatile din fișierul curent in program, mai apoi stergand entitatile din fisier
        :return:
        """
        list = Service.file_get_lines(self)
        Service.file_delete_contents(self)
        for l in list:
            l = l.split(" ")
            Service.add_entity(self, MovieService.add_movie(int(l[0]), l[1], l[2], l[3]))
