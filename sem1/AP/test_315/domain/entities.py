from dataclasses import dataclass


@dataclass
class Cafea:
    __id: int
    nume: str
    tara_de_origine: str
    pret: float

    def getId(self):
        return self.__id

    def getNume(self):
        return self.nume

    def getTaraDeOrigine(self):
        return self.tara_de_origine

    def getPret(self):
        return self.pret    

    