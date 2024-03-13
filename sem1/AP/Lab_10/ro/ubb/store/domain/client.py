from dataclasses import dataclass

from ro.ubb.store.domain.entity import Entities


@dataclass
class Client(Entities):
    __name: str
    __CNP: int

    @property
    def name(self):
        return self.__name

    @property
    def CNP(self):
        return self.__CNP

    @name.setter
    def name(self, value):
        self.__name = value

    @CNP.setter
    def CNP(self, value):
        self.__CNP = value

    def __str__(self):
        return f"{self.id} {self.__name} {self.__CNP}"
