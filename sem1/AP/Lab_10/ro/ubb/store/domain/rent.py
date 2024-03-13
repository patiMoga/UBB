from dataclasses import dataclass

from ro.ubb.store.domain.entity import Entities


@dataclass
class Rent(Entities):
    __idMovie: int
    __idClient: int
    __beginDate: str
    __endDate: str
    __returnedRent: str

    @property
    def idMovie(self):
        return self.__idMovie

    @property
    def idClient(self):
        return self.__idClient

    @property
    def beginDate(self):
        return self.__beginDate

    @property
    def endDate(self):
        return self.__endDate

    @property
    def returnedRent(self):
        return self.__returnedRent

    @idMovie.setter
    def idMovie(self, value):
        self.__idMovie = value

    @idClient.setter
    def idClient(self, value):
        self.__idClient = value

    @beginDate.setter
    def beginDate(self, value):
        self.__beginDate = value

    @endDate.setter
    def endDate(self, value):
        self.__endDate = value

    @returnedRent.setter
    def returnedRent(self, value):
        self.__returnedRent = value

    def __str__(self):
        return f"{self.id} {self.__idMovie} {self.__idClient} {self.__beginDate} {self.__endDate} {self.__returnedRent}"
