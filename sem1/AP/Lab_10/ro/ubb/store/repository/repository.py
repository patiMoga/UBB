from ro.ubb.store.exceptions.exceptions import DuplicateIdError, MissingIdError


class GenericRepository:

    def __init__(self):
        self.__all_entities = {}

    ######################## ADD ENTITY #########################

    def add_entity(self, entity):
        """
        Functia adauga parametrul 'entity' in lista curenta
        :param entity: dict
        :return:
        """
        if self.get_ID(entity.id) is not None:
            raise DuplicateIdError("Exista deja o entitate cu acest ID!")
        else:
            self.__all_entities[entity.id] = entity

    ######################## DELETE ENTITY #########################

    def delete_entity(self, id):
        """
        Functia sterge o entitate in functie de parametrul 'id'
        :param id: int
        :return:
        """
        if self.get_ID(id) is None:
            raise MissingIdError("Nu exista o entitate cu acest ID!")
        self.__all_entities.pop(id)

    ######################## MODIFY ENTITY #########################

    def modify_entity(self, newEntity):
        """
        Functia modifica o entitate din lista curenta cu alta folosind extensia '.id' din entitatea-parametru
        :param newEntity: dict
        :return:
        """
        if self.get_ID(newEntity.id) is None:
            raise MissingIdError("Nu exista o entitate cu acest ID!")
        self.__all_entities[newEntity.id] = newEntity

    ######################### PRINT ENTITY #########################

    def print_all(self):
        """
        Functia returnează valorile din lista curenta
        :return: list
        """
        return list(self.__all_entities.values())

    def get_entities(self):
        """
        Functia returnează lista curenta
        :return: dict
        """
        return self.__all_entities

    ######################### FUNCTIONS #########################

    def get_ID(self, id):
        """
        Functia returnează entitatea in functie de parametrul 'id' sau in caz contrar 'None'
        :param id: int
        :return: self.__all_entities[id] or None
        """
        if id in self.__all_entities:
            return self.__all_entities[id]
        return None
