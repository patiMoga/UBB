from ro.ubb.store.exceptions.exceptions import Validators


class Service:

    def __init__(self, entity_repository):
        self.__entity_repository = entity_repository

    ########################## ADD FUNCTION ##########################

    def add_entity(self, entity):
        """
        Functia adauga entitatea in lista curenta
        :param entity: kind of dict
        :return:
        """
        self.__entity_repository.add_entity(entity)

    ########################## MODIFY FUNCTION ##########################

    def modify_entity(self, newEntity):
        """
        Functia modifica o entitate cu o noua entitate cu un ID egal cu ID ul celei a noii entitati
        :param newEntity: kind of dict
        :return:
        """
        self.__entity_repository.modify_entity(newEntity)

    ########################## DELETE FUNCTION ##########################

    def delete_entity(self, id):
        """
        Functia sterge o entiate folosind parametrul 'id'
        :param id: int
        :return:
        """
        Validators.validate_id(id)
        self.__entity_repository.delete_entity(id)

    ########################## PRINT FUNCTION ##########################

    def get_all_entities(self):
        """
        Functia afiseaza lista curenta
        :return: list
        """
        return self.__entity_repository.print_all()

    ########################## GET-BY-ID FUNCTION ##########################

    def entity_byID(self, id):
        """
        Functia returnează entitatea dupa parametrul 'id'
        :param id: int
        :return:dict
        """
        Validators.validate_id(id)
        return self.__entity_repository.get_ID(id)

    ########################## FILE FUNCTION ##########################

    def file_get_lines(self):
        """
        Functia returnează o lista cu entitati
        :return: list
        """
        return self.__entity_repository.file_read()

    def file_delete_contents(self):
        """
        Functia sterge toate datele din fisier
        :return:
        """
        self.__entity_repository.file_delete()

        # sa traiasca comunismul boss
        # bine boss
        # schema t
        # schema 23
        # schema 72
