from ro.Patricia.Problema3.domain.entity import Entity


class Client(Entity):
    def __init__(self, idClient, name, ssn):
        Entity.__init__(self,idClient)
        self.__name = name
        self.__ssn = ssn

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getSsn(self):
        return self.__ssn

    def setSnn(self, ssn):
        self.__ssn = ssn

    def file_format(self):
        e = self.__str__()
        e = e.replace("[32m|  [0m", "")
        e = e.replace("ID: ", "")
        e = e.replace("Nume:  ", "")
        e = e.replace("CNP:", "")
        e = e.replace("\n", "")
        return e

    def __str__(self):
        return f"\u001b[32m-  \033[0mID: {Entity.get_id_entity(self)} \n" \
               f"\u001b[32m-  \033[0mNume:  {self.__name}\n" \
               f"\u001b[32m-  \033[0mCNP: {self.__ssn}\n"