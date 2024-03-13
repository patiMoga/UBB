from ro.ubb.store.domain.dto import ClientDTOAssemble
from ro.ubb.store.domain.rent import Rent
from ro.ubb.store.exceptions.exceptions import Validators
from ro.ubb.store.repository.file_repository import FileRepository
from ro.ubb.store.service.service import Service


class RentService(Service):

    def __init__(self, rent_repository: FileRepository, client_repository):
        Service.__init__(self, rent_repository)
        self.__client_repository = client_repository

    @staticmethod
    def add_rent(idRent, idMovie, idClient, beginDate, endDate, returnedRent):
        """
        Functia returnează entitatea cu datele introduse in UI
        :param idRent: int
        :param idMovie: int
        :param idClient: int
        :param beginDate: str
        :param endDate: str
        :param returnedRent: str
        :return: entity
        """
        Validators.validate_rent(idRent, idMovie, idClient, beginDate, endDate, returnedRent)
        return Rent(idRent, idMovie, idClient, beginDate, endDate, returnedRent)

    def load_from_file(self):
        """
        Functia adauga entitatile din fișierul curent in program, mai apoi stergand entitatile din fisier
        :return:
        """
        lines = Service.file_get_lines(self)
        Service.file_delete_contents(self)
        for line in lines:
            line = line.split(" ")
            Service.add_entity(self,
                               RentService.add_rent(int(line[0]), int(line[1]), int(line[2]),
                                                    line[3],
                                                    line[4], line[5]))

    ##################################################################################

    def get_movie_frequency(self):
        """
        Functia returnează un dict de frecvente ale filmelor inchiriate
        :return: dict
        """
        frequency = {}
        rents = Service.get_all_entities(self)
        for rent in rents:
            if rent.idMovie in frequency:
                frequency[rent.idMovie] += 1
            else:
                frequency[rent.idMovie] = 1
        return frequency

    def get_max_movie(self):
        """
        Functia returnează o lista cu ID-urile celor mai inchiriate filme inchiriate
        :return: list of int
        """
        id_list = []
        max_frequency = 0
        movie_frequency = self.get_movie_frequency()
        for id_movie in movie_frequency:
            if movie_frequency[id_movie] > max_frequency:
                id_list.clear()
                id_list.append(id_movie)
                max_frequency = movie_frequency[id_movie]
            elif movie_frequency[id_movie] == max_frequency:
                id_list.append(id_movie)
        return id_list

    ##################################################################################

    def get_client_frequency(self):
        """
        Functia returnează un dict de frecvente ale clienților inregistrati cu filme
        :return: dict
        """
        frequency = {}
        for rent in Service.get_all_entities(self):
            if rent.idClient in frequency:
                frequency[rent.idClient] += 1
            else:
                frequency[rent.idClient] = 1
        return frequency

    def get_client_names(self):
        """
        Functia returnează o lista cu numele tuturor clienților inregistrati cu filme
        :return: list of str
        """
        client_list = []
        client_frequency = self.get_client_frequency()
        for client in client_frequency:
            client_name = self.__client_repository.get_ID(client).name
            dto = ClientDTOAssemble.create_client_dto(client, client_name)
            client_list.append(dto)
        return client_list

    def sort_clients_by_name(self):
        """
        Functia returnează lista sortata alfabetic a numelor clienților inregistrati cu filme
        :return: list of str
        """
        client_list = self.get_client_names()
        return sorted(client_list, key=lambda d: d.name, reverse=False)

    def sort_clients_by_frequency(self):
        """
        Functia returnează o lista sortata conform frecventei clienților inregistrati cu filme
        :return: list of str
        """
        client_list = self.get_client_frequency()
        return sorted(client_list.items(), key=lambda d: d[1], reverse=True)

    def most_active_clients(self):
        """
        Funcția returnează lista cu cei mai activi clienti
        :return: list of str
        """
        client_list = []
        clients_freq = self.sort_clients_by_frequency()
        for client in clients_freq:
            client_freq = client[1]
            client_name = self.__client_repository.get_ID(client[0]).name
            dto = ClientDTOAssemble.create_client_freq_dto(client_name, client_freq)
            client_list.append(dto)
        return client_list
