from ro.Patricia.Problema3.domain.client import Client
from ro.Patricia.Problema3.domain.movie import Movie
from ro.Patricia.Problema3.domain.rent import Rent
from ro.Patricia.Problema3.repository.repository import Repository



class Service:
    def __init__(self,entity_repository : Repository):
        '''
        :param entity_repository: Repository Object
        '''
        self.__entity_repository=entity_repository

    def file_input(self):
        return self.__entity_repository.file_input()

    def file_add(self,entity):
        '''
        adauga in repository
        :param entity:
        :return:
        '''
        self.__entity_repository.file_add(entity)

    def get_all_entities(self):
        '''
        returneaza dictionarul
        :return: dict
        '''
        return self.__entity_repository.getAll()

    def get_entity_by_id(self,id_entity):
        '''
        returneaza date in functie de id
        :param id_entity: int
        :return:
        '''
        return self.__entity_repository.get_by_id(id_entity)

    def add_entity(self,entity):
        '''
        adauga in repository
        :param entity: Object
        :return:
        '''
        self.__entity_repository.add(entity)

    def update_entity(self,entity):
        '''
        modifica
        :param entity: Object
        :return:
        '''
        self.__entity_repository.modify(entity)

    def delete_entity(self,id_entity):
        '''
        sterge
        :param id_entity: int
        :return:
        '''
        self.__entity_repository.delete(id_entity)

class MovieService(Service):

    def create_movie(self,id_movie,title,description,genre):
        '''
        creeaza si returneaza o classa de file
        :param id_movie: int
        :param title: str
        :param description: str
        :param genre: str
        :return: Movie Class Object
        '''
        entity=Movie(id_movie, title, description, genre)
        return entity

    def movie_file_input(self):
        '''

        :return:
        '''
        for e in Service.file_input(self):
            e=e.split(" ")
            print(e)
            entity=self.create_movie(int(e[0]),e[1],e[2],e[3])
            Service.file_add(self,entity)

class ClientService(Service):

    def create_client(self, id_client, name, ssn):
        '''
        creeaza clasa de client si o modifica
        :param id_client: int
        :param name: str
        :param ssn: int
        :return: Client Class Object
        '''
        entity = Client(id_client, name, ssn)
        return entity

    def client_file_input(self):
        '''

        :return:
        '''
        for e in Service.file_input(self):
            e = e.split(" ")
            entity = self.create_client(int(e[0]), e[1], int(e[2]))
            Service.file_add(self, entity)

class RentService(Service):

    def __init__(self, rent_repository: Repository, *args):
        '''
        :param rent_repository: Repository Object
        :param args:
        '''
        Service.__init__(self, rent_repository)
        self.__client_repository = args[0]

    def rent_file_input(self):
        '''
        Adds entities
        :return:
        '''
        for e in Service.file_input(self):
            e = e.split(" ")
            entity = self.create_rent(int(e[0]), int(e[1]), int(e[2]), e[3], e[4])
            Service.file_add(self, entity)

    def create_rent(self, id_rent, id_client, id_movie, begin_date, end_date):
        '''
        creeaza o clasa de inchirieri
        :param id_rent: int
        :param id_client: int
        :param id_movie: int
        :param begin_date: str
        :param end_date: str
        :return: Rent Class Object
        '''
        entity = Rent(id_rent, id_client, id_movie, begin_date, end_date)
        return entity

    def getMovieFrequency(self):
        '''
        frecventa fiecarui film inchiriat
        :return:
        '''
        freq_dict = {}
        for e in list(Service.get_all_entities(self)):
            id = e.getIdMovie()
            if id in freq_dict:
                freq_dict[id] += 1
            else:
                freq_dict[id] = 1

        return freq_dict

    def maxRentMovieId(self):
        '''
       lista id filmelor care au fost cel mai des vizionate
        :return:
        '''
        freq_dict = self.getMovieFrequency()
        max_freq = 0
        id = []
        for e in freq_dict:
            if freq_dict[e] >= max_freq:
                max_freq = freq_dict[e]
                id.append(e)
        return id, max_freq

    def listLen(self, len, firstXPercent):
        '''
        calculeaza cat% a fost inchiriat un film
        :param len:
        :param firstXPercent:
        :return:
        '''
        if firstXPercent // 100 == 0:
            return (firstXPercent // 100) * len + 1
        else:
            return (firstXPercent // 100) * len

    def getClientsWithNrMoviesAndId(self):
        '''
        frecventa fiecarui client
        :return:
        '''
        freq_dict = {}
        for e in list(Service.get_all_entities(self)):
            id = e.getIdClient()
            if id in freq_dict:
                freq_dict[id] += 1
            else:
                freq_dict[id] = 1
        return freq_dict

    def getClientsAndNames(self):
        '''
        :return: List
        '''
        new_list = []
        for e in self.__client_repository.getAll():
            new_list.append({'idClient': e.get_id_entity(), 'name': e.getName()})
        return new_list

    def sortClientsByName(self, list):
        '''
        sorteaza lista dupa nume
        :param list: list of dicts
        :return: list of dicts
        '''
        return sorted(list, key=lambda d: d['name'])

    def getClientsAndMovies(self, freq_dict):
        '''

        :param freq_dict:
        :return:
        '''
        new_list = []
        for e in freq_dict:
            new_list.append({'idClient': e, 'nrMovies': freq_dict[e]})
        return new_list

    def sortClientsByNrOfMovies(self, list):
        '''
        :param list: list of dicts
        :return:
        '''
        return sorted(list, key=lambda d: d['nrMovies'], reverse=True)

    def mostActiveClient(self):
        '''
       returneaza primii 20% clienti in funtie de activitatea lor
        :return:
        '''
        new_list = self.sortClientsByNrOfMovies(self.getClientsAndMovies(self.getClientsWithNrMoviesAndId()))
        new_list = new_list[:self.listLen(len(new_list), 20)]
        return new_list

    def clientsOrderedByNrOfMovies(self):
        '''
        Returneaza lista clientilor in functie de cate filme au inchiriat
        :return:
        '''
        new_list = self.sortClientsByNrOfMovies(self.getClientsAndMovies(self.getClientsWithNrMoviesAndId()))
        new_list = new_list[:self.listLen(len(new_list), 100)]
        return new_list

    def clientsOrderedByName(self):
        return self.sortClientsByName(self.getClientsAndNames())

    def mostRentedMovie(self):
        '''
       Returneaza lista de filme dupa id care au fost inchiriate cel mai frecvent
        :return:
        '''
        maxRentMovieIds, frequency = self.maxRentMovieId()
        return maxRentMovieIds, frequency