from dataclasses import dataclass


@dataclass
class Entities:
    __id: int

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
