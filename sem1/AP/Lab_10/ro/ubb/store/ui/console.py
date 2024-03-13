import itertools
import sys

from ro.ubb.store.exceptions.exceptions import EntityError


class Console:

    def __init__(self, movie_service, client_service, rent_service):
        self.__movie_service = movie_service
        self.__client_service = client_service
        self.__rent_service = rent_service

    #################################### UI.FILE_INPUT/OUTPUT ####################################

    def file_load(self):
        self.__movie_service.load_from_file()
        self.__client_service.load_from_file()
        self.__rent_service.load_from_file()
        print("\x1b[32mDatele din cloud au fost descarcate in program!\x1b[0m")

    #################################### UI.ADD ####################################

    def addMovie(self):
        try:
            id = input("Introduceti ID-ul filmului: ")
            title = input("Introduceti numele filmului: ")
            description = input("Introduceti descrierea filmului: ")
            genre = input("Introduceti genul fimului: ")
            self.__movie_service.add_entity(self.__movie_service.add_movie(int(id), title, description, genre))
        except EntityError as err:
            print("\n\x1b[31mDate invalide!\x1b[0m", err)

    def addClient(self):
        try:
            id = input("Introduceti ID-ul clientului: ")
            name = input("Introduceti numele clientului: ")
            CNP = input("Introduceti CNP-ul clientului: ")
            self.__client_service.add_entity(self.__client_service.add_client((int(id), name, int(CNP))))
        except EntityError as err:
            print("\n\x1b[31mDate invalide!\x1b[0m", err)

    def addRent(self):
        print("-----------------------------------------------------\n")
        self.printMovies()
        print("\n-----------------------------------------------------\n")
        self.printClients()
        print("\n-----------------------------------------------------\n")
        try:
            id = input("Introduceti ID-ul inchirierei: ")
            idMovie = input("Introduceti ID-ul filmului: ")
            idClient = input("Introduceti ID-ul clientului: ")
            beginDate = input("Introduceti data check-in inchiriere (sub forma zz/ll/aaaa) : ")
            endDate = input("Introduceti data check-out inchiriere (sub forma zz/ll/aaaa) : ")
            returnedRent = input("FILM RETURNAT | YES/NO : ")
            self.__rent_service.add_entity(self.__rent_service.add_rent((int(id), int(idMovie), int(idClient),
                                                                        beginDate, endDate, returnedRent)))
        except EntityError as err:
            print("\n\x1b[31mDate invalide!\x1b[0m", err)

    #################################### UI.PRINT ####################################

    @staticmethod
    def entity_format(entity):
        entity = str(entity)
        entity = entity.strip()
        return entity.split(" ")

    @staticmethod
    def format_movie(movie):
        movie = Console.entity_format(movie)
        print(f" | ID film: {movie[0]}\n"
              f" | Titlu film: {movie[1]}\n"
              f" | Descriere film: {movie[2]}\n"
              f" | Gen film: {movie[3]}\n")

    @staticmethod
    def format_client(client):
        client = Console.entity_format(client)
        print(f" | ID client: {client[0]}\n"
              f" | Nume client: {client[1]}\n"
              f" | CNP client: {client[2]}\n")

    @staticmethod
    def format_rent(rent):
        rent = Console.entity_format(rent)
        print(f" | ID inregistrare: {rent[0]}\n"
              f" | ID film: {rent[1]}\n"
              f" | ID client: {rent[2]}\n"
              f" | Data film preluare: {rent[3]}\n"
              f" | Data film returnare: {rent[4]}\n"
              f" | Film returnat: {rent[5]}\n")

    def printMovies(self):
        movie_list = self.__movie_service.get_all_entities()
        if not movie_list:
            print("\x1b[33mNu exista filme in baza de date!\x1b[0m")
        for movie in movie_list:
            Console.format_movie(movie)

    def printClients(self):
        client_list = self.__client_service.get_all_entities()
        if not client_list:
            print("\x1b[33mNu exista clienti in baza de date!\x1b[0m")
        for client in client_list:
            Console.format_client(client)

    def printRents(self):
        rent_list = self.__rent_service.get_all_entities()
        if not rent_list:
            print("\x1b[33mNu exista închirieri in baza de date!\x1b[0m")
        for rent in rent_list:
            Console.format_rent(rent)

    #################################### UI.MODIFY ####################################

    def modifyMovies(self):
        print("-----------------------------------------------------\n")
        self.printMovies()
        print("\n-----------------------------------------------------\n")
        try:
            id = input("Introduceti ID-ul filmului: ")
            newTitle = input("Introduceti noul numele al filmului: ")
            newDescription = input("Introduceti noua descrierea a filmului: ")
            newGenre = input("Introduceti noul gen al fimului: ")
            self.__movie_service.modify_entity(self.__movie_service.add_movie
                                               (int(id), newTitle, newDescription, newGenre))
        except EntityError as err:
            print("\n\x1b[31mDate invalide!\x1b[0m", err)

    def modifyClient(self):
        print("-----------------------------------------------------\n")
        self.printClients()
        print("\n-----------------------------------------------------\n")
        try:
            id = input("Introduceti ID-ul clientului: ")
            newName = input("Introduceti noul nume al clientului: ")
            newCNP = input("Introduceti noul CNP al clientului: ")
            self.__client_service.modify_entity(self.__client_service.add_client((int(id), newName, int(newCNP))))
        except EntityError as err:
            print("\n\x1b[31mDate invalide!\x1b[0m", err)

    def modifyRent(self):
        print("-----------------------------------------------------\n")
        self.printRents()
        print("\n-----------------------------------------------------\n")
        try:
            id = input("Introduceti ID-ul inchirierii: ")
            idMovie = input("Introduceti ID-ul filmului: ")
            idClient = input("Introduceti ID-ul clientului: ")
            beginDate = input("Introduceti data check-in inchiriere (sub forma zz/ll/aaaa) : ")
            endDate = input("Introduceti data check-out inchiriere (sub forma zz/ll/aaaa) : ")
            returnedRent = input("FIlM RETURNAT | YES/NO : ")

            self.__rent_service.modify_entity(self.__rent_service.add_rent
                                              ((int(id), int(idMovie), int(idClient),
                                                beginDate, endDate, returnedRent)))
        except EntityError as err:
            print("\n\x1b[31mDate invalide!\x1b[0m", err)

    #################################### UI.DELETE ####################################

    def deleteMovie(self):
        print("-----------------------------------------------------\n")
        self.printMovies()
        print("\n-----------------------------------------------------\n")
        try:
            id = input("Introduceti ID-ul filmului ce trebuie sters: ")
            self.__movie_service.delete_entity(int(id))
        except EntityError as err:
            print("\n\x1b[31mDate invalide!\x1b[0m", err)

    def deleteClient(self):
        print("-----------------------------------------------------\n")
        self.printClients()
        print("\n-----------------------------------------------------\n")
        try:
            id = input("Introduceti ID-ul clientului ce trebuie sters: ")
            self.__client_service.delete_entity(int(id))
        except EntityError as err:
            print("\n\x1b[31mDate invalide!\x1b[0m", err)

    def deleteRent(self):
        print("-----------------------------------------------------\n")
        self.printRents()
        print("\n-----------------------------------------------------\n")
        try:
            id = input("Introduceti ID-ul rentului ce trebuie sters: ")
            self.__rent_service.delete_entity(int(id))
        except EntityError as err:
            print("\n\x1b[31mDate invalide!\x1b[0m", err)

    #################################### UI.SEARCH ####################################

    def searchMovie(self):
        try:
            id = input("Introduceti ID-ul filmului dorit: ")
            Console.format_movie(self.__movie_service.entity_byID(int(id)))
        except EntityError as err:
            print("\n\x1b[31mDate invalide!\x1b[0m", err)

    def searchClient(self):
        try:
            id = input("Introduceti ID-ul clientului dorit: ")
            Console.format_client(self.__client_service.entity_byID(int(id)))
        except EntityError as err:
            print("\n\x1b[31mDate invalide!\x1b[0m", err)

    def searchRent(self):
        try:
            id = input("Introduceti ID-ul inchirierii dorit: ")
            Console.format_rent(self.__rent_service.entity_byID(int(id)))
        except EntityError as err:
            print("\n\x1b[31mDate invalide!\x1b[0m", err)

    #################################### UI.REPORTS ####################################

    def order_ClientsName(self):
        print("Clientii ce au inchiriat filme dupa nume:\n")
        client_list = self.__rent_service.sort_clients_by_name()
        for client in client_list:
            print("ID client:", client.id, " - ", client.name)

    def order_ClientsRentedMovies(self):
        print("Clientii ce au inchiriat filme dupa numarul de filme inchiriate:\n")
        client_list = self.__rent_service.sort_clients_by_frequency()
        for client in itertools.islice(client_list, 3):
            print(self.__client_service.entity_byID(client[0]).name, " : ", client[1])

    def order_MostRentedMovies(self):
        print("Cele mai inchiriate filme:\n")
        for id_movie in self.__rent_service.get_max_movie():
            print(self.__movie_service.entity_byID(id_movie).title)

    def order_ActiveClients(self):
        print("Cei mai activi clienti:\n")
        for client in itertools.islice(self.__rent_service.most_active_clients(), 3):
            print(client.name, " : ", client.freq)

    #################################### UI.REPORT_MENU ####################################

    def order_Clients(self):
        options = {"1": self.order_ClientsName,
                   "2": self.order_ClientsRentedMovies,
                   "R": self.returnMenu}

        print("1 - Afiseaza o lista cu toti clientii ordonati alfabetic\n"
              "2 - Afiseaza o lista cu toti clientii ordonati dupa numarul de filme imprumutate\n"
              "R - Intoarcere la meniu.\n")

        opt = input("Comanda aleasa: ")
        print("\n")
        try:
            options[opt]()
        except KeyError as ve:
            print("\x1b[31mOptiunea aleasa nu exista! : \x1b[0m", ve)

    def reportMenu(self):
        options = {"1": self.order_Clients,
                   "2": self.order_MostRentedMovies,
                   "3": self.order_ActiveClients,
                   "R": self.returnMenu}

        print("1 - Ordonare clienti.\n"
              "2 - Cele mai inchiriate filme.\n"
              "3 - Cei mai activi clienti.\n"
              "R - Intoarcere la meniul principal.\n")

        opt = input("Comanda aleasa: ")
        print("\n")
        try:
            options[opt]()
        except KeyError as ve:
            print("\x1b[31mOptiunea aleasa nu exista! : \x1b[0m", ve)

    #################################### UI.MOVIE_MENU ####################################

    @staticmethod
    def print_movie_menu():
        print("\n1 - Adauga un nou film.\n"
              "2 - Modifica film in lista de filme.\n"
              "3 - Sterge un film din lista de filme.\n"
              "4 - Afiseaza film dupa ID.\n"
              "5 - Afiseaza lista de filme inregistrate.\n"
              "R - Intoarcere la meniul principal\n")

    def movieMenu(self):
        options = {"1": self.addMovie,
                   "2": self.modifyMovies,
                   "3": self.deleteMovie,
                   "4": self.searchMovie,
                   "5": self.printMovies,
                   "R": self.returnMenu}

        self.print_movie_menu()

        opt = input("Comanda aleasa: ")

        print("\n")
        try:
            options[opt]()
        except KeyError as ve:
            print("\x1b[31mOptiunea aleasa nu exista! : \x1b[0m", ve)

    #################################### UI.CLIENT_MENU ####################################

    @staticmethod
    def print_client_menu():
        print("\n1 - Adauga un nou client.\n"
              "2 - Modifica client in lista de clienti.\n"
              "3 - Sterge un client din lista de clienti.\n"
              "4 - Afiseaza client dupa ID.\n"
              "5 - Afiseaza lista de clienti inregistrati.\n"
              "R - Intoarcere la meniul principal\n")

    def clientMenu(self):
        options = {"1": self.addClient,
                   "2": self.modifyClient,
                   "3": self.deleteClient,
                   "4": self.searchClient,
                   "5": self.printClients,
                   "R": self.returnMenu}

        self.print_client_menu()

        opt = input("Comanda aleasa: ")

        print("\n")
        try:
            options[opt]()
        except KeyError as ve:
            print("\x1b[31mOptiunea aleasa nu exista! : \x1b[0m", ve)

    #################################### UI.RENT_MENU ####################################

    @staticmethod
    def print_opt_rent():
        print("Optiuni:\n\n"
              "1 - Adauga o noua inchiriere de film.\n"
              "2 - Modifica o inchiriere de film.\n"
              "3 - Sterge închirierea de film.\n"
              "4 - Afiseaza inchiriere film dupa ID.\n"
              "5 - Afiseaza toate inchirierile.\n"
              "R - Întoarcere la meniul principal.\n")

    def rentMenu(self):
        options = {"1": self.addRent,
                   "2": self.modifyRent,
                   "3": self.deleteRent,
                   "4": self.searchRent,
                   "5": self.printRents,
                   "R": self.returnMenu}

        self.print_opt_rent()

        opt = input("Comanda aleasa: ")

        print("\n")
        try:
            options[opt]()
        except KeyError as ve:
            print("\x1b[31mOptiunea aleasa nu exista! : \x1b[0m", ve)

    #################################### UI.STATIC FUNTIONS ####################################

    @staticmethod
    def exit_Program():
        sys.exit("\x1b[35mAuf Wiedersehen!\x1b[0m")

    @staticmethod
    def returnMenu():
        return

    #################################### UI.MAIN_MENU ####################################

    @staticmethod
    def print_options():
        print("\nOptiuni:\n\n"
              "1 - Meniu Filme.\n"
              "2 - Meniu Clienti.\n"
              "3 - Meniu Închirieri\n"
              "4 - Rapoarte.\n"
              "5 - Incarcare date din cloud.\n"
              "X - Iesire din program.\n")

    def run_console(self):
        while True:
            main_options = {"1": self.movieMenu,
                            "2": self.clientMenu,
                            "3": self.rentMenu,
                            "4": self.reportMenu,
                            "5": self.file_load,
                            "X": self.exit_Program}
            self.print_options()

            opt = input("Comanda aleasa: ")

            try:
                main_options[opt]()
            except KeyError as ve:
                print("\x1b[31mOptiunea aleasa nu exista! : \x1b[0m", ve)
