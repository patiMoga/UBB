from ro.ubb.store.exceptions.exceptions import DuplicateIdError, MissingIdError
from ro.ubb.store.repository.repository import GenericRepository


class FileRepository(GenericRepository):
    def __init__(self, path):
        super().__init__()
        self.__entities = GenericRepository.get_entities(self)
        self.__path = path

    def file_read(self):
        """
        Functia returnează lista cu entitatile citite din fișierul curent
        :return: list
        """
        with open(f"repository/text_files/{self.__path}", "r") as file:
            file_list = file.readlines()
            for line, e in enumerate(file_list):
                file_list[line] = e.strip()
            return file_list

    def file_append_entity(self, entity):
        """
        Functia adauga entitatile din fișierul curent
        :param entity: dict
        :return:
        """
        with open(f"repository/text_files/{self.__path}", "a") as file:
            file.write(str(entity))
            file.write('\n')

    def file_delete_entity(self, id):
        """
        Functia sterge entitatea din fișierul curent cu 'id'-ul egal cu parametrul 'id'
        :param id: int
        :return:
        """
        del_line = self.get_file_line_by_id(id)
        with open(f'repository/text_files/{self.__path}', 'r') as file:
            file_list = file.readlines()
        with open(f'repository/text_files/{self.__path}', 'w') as file:
            for entity in file_list:
                entity = entity.strip()
                if entity != del_line:
                    file.write(entity)
                    file.write('\n')

    def file_delete(self):
        """
        Functia sterge toate entitatile din fișierul curent
        :return:
        """
        with open(f'repository/text_files/{self.__path}', 'w') as file:
            file.truncate(0)

    def get_file_line_by_id(self, id):
        """
        Functia returnează entitate din fișierul curent folosind parametrul 'id'
        :param id: int
        :return: line or None
        """
        with open(f'repository/text_files/{self.__path}', 'r') as file:
            file_list = file.readlines()
            for line in file_list:
                line = line.strip()
                linie = line.split(" ")
                if int(linie[0]) == id:
                    return line
        return None

    def add_entity(self, entity):
        """
        Functia adauga parametrul 'entity' in lista curenta
        :param entity: dict
        :return:
        """
        if self.get_ID(entity.id) is not None:
            raise DuplicateIdError("Exista deja o entitate cu acest ID!")
        self.file_append_entity(entity)
        self.__entities[entity.id] = entity

    def modify_entity(self, entity):
        """
        Functia modifica o entitate din lista curenta cu alta folosind extensia '.id' din entitatea-parametru
        :param entity: dict
        :return:
        """
        if self.get_ID(entity.id) is None:
            raise MissingIdError("Nu exista o entitate cu acest ID!")
        self.__entities[entity.id] = entity

    def delete_entity(self, id):
        """
        Functia sterge o entitate in functie de parametrul 'id'
        :param id: int
        :return:
        """
        if self.get_ID(id) is None:
            raise MissingIdError("Nu exista o entitate cu acest ID!")
        self.file_delete_entity(id)
        self.__entities.pop(id)
