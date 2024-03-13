class EntityError(Exception):
    pass


class IdError(EntityError):
    pass


class MissingIdError(IdError):
    pass


class DuplicateIdError(IdError):
    pass


class FormatIdError(IdError):
    pass


class StringFormatError(EntityError):
    pass


class CNPFormatError(EntityError):
    pass


class Validators:

    @staticmethod
    def validate_movie(id, title, description, genre):
        """
        Functia validează datele filmului
        :param id: int
        :param title: str
        :param description: str
        :param genre: str
        :return:
        """
        Validators.validate_id(id)
        Validators.validate_string(title)
        Validators.validate_string(description)
        Validators.validate_string(genre)

    @staticmethod
    def validate_client(idClient, name, CNP):
        """
        Functia validează datele clientului
        :param idClient: int
        :param name: str
        :param CNP: int
        :return:
        """
        Validators.validate_id(idClient)
        Validators.validate_string(name)
        Validators.validate_CNP(CNP)

    @staticmethod
    def validate_rent(id_rent, id_client, id_movie, beginDate, endDate, ret_rent):
        """
        Functia validează datele inchirierii
        :param id_rent: int
        :param id_client: int
        :param id_movie: int
        :param beginDate: str
        :param endDate: str
        :param ret_rent: str
        :return:
        """
        Validators.validate_id(id_rent)
        Validators.validate_id(id_client)
        Validators.validate_id(id_movie)
        Validators.validate_string(beginDate)
        Validators.validate_string(endDate)
        Validators.validate_string(ret_rent)

    @staticmethod
    def validate_id(id):
        """
        Functia validează daca parametrul 'id_entity' este de tip int, contrar transmite un mesaj eroare
        :param id: int
        :return:
        """
        if not isinstance(id, int):
            raise FormatIdError("ID trebuie sa fie un numar de tip integer!")

    @staticmethod
    def validate_string(string):
        """
        Functia validează daca parametrul 'string' este de tip str, contrar transmite un mesaj de eroare
        :param string:
        :return:
        """
        if string == "":
            raise StringFormatError("Titlul/Descrierea/Nume/Genul trebuie sa fie cel putin un caracter!")

    @staticmethod
    def validate_CNP(CNP):
        """
        Functia verifica daca parametrul CNP este YES sau NO
        :param CNP: int
        :return:
        """
        if not isinstance(CNP, int):
            raise CNPFormatError("CNP trebuie sa fie cel putin un numar intreg!")
