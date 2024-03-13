import sys

from ro.Patricia.Problema3.exceptions.exceptions import DuplicateIdError
from ro.Patricia.Problema3.service.service import MovieService
from ro.Patricia.Problema3.service.service import ClientService
from ro.Patricia.Problema3.service.service import RentService


class Console:
    def __init__(self, clientService: ClientService, movieService: MovieService, rentMovieService:RentService):
        self.__client_service = clientService
        self.__movie_service = movieService
        self.__rent_service=rentMovieService

    def printMenu(self):
         print(
                """\u001b[32mI. Comenzi pentru gestiunea listei\033[0m
    1. Adaugare                          
    2. Stergere                                           
    3. Modificare                                               
    4. Afisare  \u001b[32m 
II. Cautare\033[0m 
    5. Cautare  \u001b[32m 
III.Inscrieri  \033[0m
    6. Inscriere Persoana \u001b[32m
IV.Rapoarte \033[0m
    7. Statistici
                \u001b[32m 
    8. File imput
    x. Exit\n""")
    def file_input_submenu(self):
        try:
            options = {"1": self.file_input_movies,
                       "2": self.file_input_clients,
                       "3": self.file_input_rents }

            print("\n\u001b[32m1.\033[0m    Incarca Date din repo Filme\n"
                  "\u001b[32m2.\033[0m    Incarca Date din repo Clienti\n"
                  "\u001b[32m3.\033[0m    Incarca Date din repo Inchirieri")
            option = input("Optiunea aleasa: ")
            options[option]()
        except KeyError:
            print("\u001b[32mOptiunea aleasa nu exista !!!")

    def file_input_movies(self):
        try:
            self.__movie_service.movie_file_input()
        except ValueError:
            print("\u001b[32m Ooops nu am reusit sa obtinem valorile din repo!!!")

    def file_input_clients(self):
        try:
            self.__client_service.client_file_input()
        except ValueError:
            print("\u001b[32m Ooops nu am reusit sa obtinem valorile din repo!!!")

    def file_input_rents(self):
        try:
            self.__rent_service.rent_file_input()
        except ValueError:
            print("\u001b[32m Ooops nu am reusit sa obtinem valorile din repo!!!")

    def addSubMenu(self):
        try:
            options = {"1": self.addMovie, "2": self.addClient}
            print("\n\u001b[32m1.\033[0m  Adauga film\n"
                  "\u001b[32m2.\033[0m  Adauga client")
            option = input("Optiunea aleasa: ")
            options[option]()
        except KeyError:
            print("\u001b[32mOptiunea aleasa nu exista !!!")


    def addMovie(self):
        try:
            idMovie=int(input("Insereaza id-ul filmului: "))
            title=input("Titlul filmului: ")
            description=input("Descrierea filmului: ")
            author=input("Genul filmului: ")
            self.__movie_service.add_entity(self.__movie_service.create_movie(idMovie, title, description, author))
        except ValueError:
            print("\u001b[32m Id-ul trebuie sa fie format doar din cifre !!!")
        except DuplicateIdError as ke:
            print(ke)

    def addClient(self):
        try:
            idClient = int(input("Insereaza id-ul clientului: "))
            name = input("Numele clientului: ")
            ssn = int(input("CNP: "))
            self.__client_service.add_entity(self.__client_service.create_client(idClient, name, ssn))
        except ValueError:
            print("\u001b[32m Id-ul si CNP trebuie sa fie format doar din cifre !!!")
        except DuplicateIdError as ke:
            print(ke)


    def deleteSubMenu(self):
        try:
            options = {"1": self.deleteMovie, "2": self.deleteClient}
            print("\n\u001b[32m1.\033[0m  Sterge film\n"
                  "\u001b[32m2.\033[0m  Sterge client")
            option = input("Optiunea aleasa: ")
            options[option]()
        except KeyError:
            print("\u001b[32mOptiunea aleasa nu exista !!!")

    def deleteMovie(self):
        try:
            idMovie = int(input("Insereaza id-ul filmului: "))
            self.__movie_service.delete_entity(idMovie)
        except ValueError:
            print("\u001b[32m Id-ul trebuie sa fie format doar din cifre !!!")
        except KeyError as ke:
            print(ke)

    def deleteClient(self):
        try:
            idClient = int(input("Insereaza id-ul clientului: "))
            self.__client_service.delete_entity(idClient)
        except ValueError:
            print("\u001b[32m Id-ul trebuie sa fie format doar din cifre !!!")
        except KeyError as ke:
            print(ke)

    def modifySubMenu(self):
        try:
            options={"1":self.modifyMovie, "2":self.modifyClient}
            print("\n\u001b[32m1.\033[0m  Modifica film\n"
                  "\u001b[32m2.\033[0m  Modifica client")
            option=input("Optiunea aleasa: ")
            options[option]()
        except KeyError:
            print("\u001b[32mOptiunea aleasa nu exista !!!")


    def modifyMovie(self):
        try:
            idMovie = int(input("Insereaza id-ul filmului: "))
            newTitle = input("Titlul filmului: ")
            newDescription = input("Descrierea filmului: ")
            newAuthor = input("Genul filmului: ")
            self.__movie_service.update_entity(self.__movie_service.create_movie(idMovie, newTitle, newDescription, newAuthor))
        except ValueError:
            print("\u001b[32m Id-ul trebuie sa fie format doar din cifre !!!")
        except KeyError as ke:
            print(ke)

    def modifyClient(self):
        try:
            idClient = int(input("Insereaza id-ul clientului: "))
            newName = input("Numele clientului: ")
            newSsn = int(input("CNP: "))
            self.__client_service.update_entity(self.__client_service.create_client(idClient, newName, newSsn))
        except ValueError:
            print("\u001b[32m Id-ul si CNP trebuie sa fie format doar din cifre !!!")
        except KeyError as ke:
            print(ke)

    def lookupSubMenu(self):
        try:
            options = {"1": self.lookupMovie, "2": self.lookupClient}
            print("\n\u001b[32m1.\033[0m  Cauta film\n"
                  "\u001b[32m2.\033[0m  Cauta client")
            option = input("Optiunea aleasa: ")
            options[option]()
        except KeyError:
            print("\u001b[32mOptiunea aleasa nu exista !!!")


    def lookupMovie(self):
        try:
            idMovie=int(input("Inserati id film: "))
            print(self.__movie_service.get_entity_by_id(idMovie))
        except ValueError:
            print("\u001b[32m Id-ul trebuie sa fie format doar din cifre !!!")
        except KeyError as ke:
            print(ke)

    def lookupClient(self):
        try:
            idClient = int(input("Inserati id client: "))
            print(self.__client_service.get_entity_by_id(idClient))
        except ValueError:
            print("\u001b[32m Id-ul trebuie sa fie format doar din cifre !!!")
        except KeyError as ke:
            print(ke)

    def printAllSubMenu(self):
        try:
            options = {"1": self.printAllMovies, "2": self.printAllClients}
            print("\n\u001b[32m1.\033[0m  Afiseaza filme\n"
                  "\u001b[32m2.\033[0m  Afiseaza clienti")
            option = input("Optiunea aleasa: ")
            options[option]()
        except KeyError:
            print("\u001b[32mOptiunea aleasa nu exista !!!")


    def printAllMovies(self):
        for entity in self.__movie_service.get_all_entities():
            print(entity)

    def printAllClients(self):
        for entity in self.__client_service.get_all_entities():
            print(entity)

    def signup(self):
        try:
            idRent=int(input("Insereaza id imprumut: "))
            idMovie = int(input("Insereaza id film imprumutat: "))
            idClient = int(input("Insereaza id client ce imprumuta filmul: "))
            print("\u001b[32m!!!\033[0m Datile trebuie sa fie sub forma: dd/mm/yyyy")
            beginDate=input("Data inceput imprumut: ")
            endDate=input("Data sfarsit imprumut: ")
            self.__rent_service.add_entity(self.__rent_service.create_rent(idRent, idMovie, idClient, beginDate, endDate))
        except ValueError:
            print("\u001b[32m Id-ul trebuie sa fie format doar din cifre !!!")
        except KeyError as ke:
            print(ke)

    def mostRentedMovie(self):
        print("\u001b[32m| \033[0mCele mai inchiriate filme sunt: \n")
        ids, frequency = self.__rent_service.mostRentedMovie()
        for id in ids:
            print(self.__movie_service.get_entity_by_id(id))

        print(f"\u001b[32m| \033[0mFiecare film a fost inchiriata de: {frequency} persoane\n")

    def orderClientsSubMenu(self):
        try:
            options = {"1": self.orderClientsByName, "2": self.orderClientsByRentedMovies}
            print("\n\u001b[32m1.\033[0m  Afiseaza o lista cu toti clientii ordonati alfabetic\n"
                  "\u001b[32m2.\033[0m  Afiseaza o lista cu toti clientii ordonati dupa numarul de filme imprumutate")
            option = input("Optiunea aleasa: ")
            options[option]()
        except KeyError:
            print("\u001b[32mOptiunea aleasa nu exista !!!")

    def orderClientsByName(self):
        new_list = self.__rent_service.clientsOrderedByName()
        for e in new_list:
            print(self.__client_service.get_entity_by_id(e['idClient']))

    def orderClientsByRentedMovies(self):
        new_list = self.__rent_service.clientsOrderedByNrOfMovies()
        for e in new_list:
            print(self.__client_service.get_entity_by_id(e['idClient']),
                  f"\u001b[32m-> \033[0mEi au inchiriat: {e['nrMovies']} filme\n")

    def mostActiveClients(self):
        print("\u001b[32m| \033[0mCei mai activi 20% clienti sunt: \n")
        new_list = self.__rent_service.mostActiveClient()
        for e in new_list:
            print(self.__client_service.get_entity_by_id(e['idClient']),
                  f"\u001b[32m-> \033[0mEi au inchiriat: {e['nrMovies']} filme\n")

    def printAllRents(self):
        for entity in self.__rent_service.get_all_entities():
            print(entity)

    def statisticsSubMenu(self):
        try:
            options={"1":self.mostRentedMovie
                     ,"2":self.orderClientsSubMenu
                     ,"3":self.mostActiveClients
                     ,"4":self.printAllRents}
            print("\n\u001b[32m1.\033[0m  Cel mai inchiriat film\n"
                  "\u001b[32m2.\033[0m  Ordonare clienti\n"
                  "\u001b[32m3.\033[0m  Cei mai activi clienti\n"
                  "\u001b[32m4.\033[0m  Afiseaza toate imprumuturile")
            option=input("Optiunea Aleasa: ")
            options[option]()
        except KeyError:
            print("\u001b[32mOptiunea aleasa nu exista !!!")

    def exit(self):
        sys.exit("\u001b[32m Va multumim ca ati ales sa folositi aceasta aplicatie !!!")

    def menu(self):
        while True:
            try:
                options={ "1":self.addSubMenu
                         ,"2":self.deleteSubMenu
                         ,"3":self.modifySubMenu
                         ,"4":self.printAllSubMenu
                         ,"5":self.lookupSubMenu
                         ,"6":self.signup
                         ,"7":self.statisticsSubMenu
                         ,"8":self.file_input_submenu
                         ,"x":self.exit}
                self.printMenu()
                option = input("Optiunea aleasa: ")
                option =option.lower()
                options[option]()
            except KeyError:
                print("\u001b[32mOptiunea aleasa nu exista !!!")


