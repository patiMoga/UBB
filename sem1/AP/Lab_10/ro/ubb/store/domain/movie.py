from dataclasses import dataclass

from ro.ubb.store.domain.entity import Entities


@dataclass
class Movie(Entities):
    __title: str
    __description: str
    __genre: str

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def genre(self):
        return self.__genre

    @title.setter
    def title(self, value):
        self.__title = value

    @description.setter
    def description(self, value):
        self.__description = value

    @genre.setter
    def genre(self, value):
        self.__genre = value

    def __str__(self):
        return f"{self.id} {self.__title} {self.__description} {self.__genre}"