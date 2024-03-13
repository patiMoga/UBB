import random

from service.cafea_service import CafeaService


class CafeaConsole:
    def __init__(self, cafea_service: CafeaService):
        self.__cafea_service = cafea_service

    def menu(self):
        print("1. Adauga \n"
              "2. Afiseaza")

    def adauga_cafea(self):
        try:
            id = random.randint(1, 100)
            nume = input("Nume = ")
            tara_de_origine = input("Tara = ")
            pret = float(input("Pret = "))

            if pret > 0:
                self.__cafea_service.add(id, nume, tara_de_origine, pret)
            else:
                raise ValueError("Pretul trebuie sa fie mai mare ca 0")
        except ValueError as ve:
            print(ve)

    def print_cafea(self):
        cafele = self.__cafea_service.getAll()

        for cafea in cafele:
            print(cafea)

    def sortare(self):
        print(self.__cafea_service.sortare())

    def filtrare(self):
        try:
            tara = input("Tara = ")
            pret = input("Pret = ")

            print(self.__cafea_service.filtrare(tara, pret))
        except ValueError as ve:
            print(ve)


    def run_console(self):
        while True:
            self.menu()
            opt = input("Alege optiunea = ")

            if opt == "1":
                self.adauga_cafea()
            elif opt == "2":
                self.print_cafea()
            elif opt == "3":
                self.sortare()
            elif opt == "4":
                self.filtrare()


