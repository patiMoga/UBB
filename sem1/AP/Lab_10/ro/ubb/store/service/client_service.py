from ro.ubb.store.domain.client import Client
from ro.ubb.store.exceptions.exceptions import Validators
from ro.ubb.store.service.service import Service


class ClientService(Service):

    @staticmethod
    def add_client(idClient, name, CNP):
        """
        Functia returnează entitatea cu datele introduse in UI
        :param idClient: int
        :param name: str
        :param CNP: int
        :return: entity
        """
        Validators.validate_client(idClient, name, CNP)
        return Client(idClient, name, CNP)

    def load_from_file(self):
        """
        Functia adauga entitatile din fișierul curent in program, mai apoi stergand entitatile din fisier
        :return:
        """
        list = Service.file_get_lines(self)
        Service.file_delete_contents(self)
        for l in list:
            l = l.split(" ")
            Service.add_entity(self, ClientService.add_client(int(l[0]), l[1], int(l[2])))
