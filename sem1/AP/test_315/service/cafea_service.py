from domain.entities import Cafea
from repository.cafea_repository import Repository


class CafeaService:
    def __init__(self, cafea_repository: Repository):
        self.cafea_repository = cafea_repository

    def add(self, id, nume, tara_de_origine, pret):
        """
        Adauga o cafea
        :param id: random int
        :param nume: str
        :param tara_de_origine: str
        :param pret: float
        :return: Adauga o cafea
        """
        cafea = Cafea(id, nume, tara_de_origine, pret)
        self.cafea_repository.addCofee(cafea)

    def getAll(self):
        """
        Returneaza toate cafelele
        :return: cafele
        """
        return self.cafea_repository.getAll()

    def sortare(self):
        """
        Sorteaza cafele dupa tara si pret
        :return: o lista cu cafele sortate
        """
        cafele = self.getAll()
        cafele = sorted(cafele, key= lambda x: (x.tara_de_origine, x.pret))

        return cafele


    def filtrare(self, tara_ui, pret_ui):
        """
        Returneaza o lista de cafele cu o tara anume cu un pret mai mic decat acel dat
        :param tara_ui: str
        :param pret_ui: str
        :return: o lista cu cafele
        """
        slot = []
        cafele = self.getAll()

        if tara_ui == "":
            for cafea in cafele:
                if cafea.getPret() < float(pret_ui):
                    slot.append(cafea)

        if pret_ui == "":
            for cafea in cafele:
                if cafea.getTaraDeOrigine() == tara_ui:
                    slot.append(cafea)

        if tara_ui == ""  and pret_ui == "":
            raise ValueError("Adauga ceva!")

        for cafea in cafele:
            if cafea.getTaraDeOrigine() == tara_ui and cafea.getPret() < float(pret_ui):
                slot.append(cafea)

        return slot



