from ro.Patricia.Problema3.domain.entity import Entity


class Rent(Entity):
    def __init__(self, idRent, idMovie, idClient, beginDate, endDate):
        Entity.__init__(self,idRent)
        self.__idMovie=idMovie
        self.__idClient=idClient
        self.__beginDate=beginDate
        self.__endDate=endDate

    def getIdMovie(self):
        return self.__idMovie

    def setIdMovie(self, idMovie):
        self.__idMovie = idMovie

    def getIdClient(self):
        return self.__idClient

    def setIdClient(self, idClient):
        self.__idClient = idClient

    def getBeginDate(self):
        return self.__beginDate

    def setBeginDate(self, beginDate):
        self.__beginDate = beginDate

    def getEndDate(self):
        return self.__endDate

    def setEndDate(self, endDate):
        self.__endDate = endDate

    def file_format(self):
        e = self.__str__()
        e = e.replace("[36m|  [0m", "")
        e=e.replace("ID inchiriere: ","")
        e = e.replace("ID carte: ", "")
        e = e.replace("ID client:  ", "")
        e = e.replace("Data inceput:", "")
        e=e.replace("Data sfarsit: ","")
        e = e.replace("\n", "")
        return e

    def __str__(self):
        return f"\u001b[32m-  \033[0mID Inchiriere: {Entity.get_id_entity(self)} \n"\
               f"\u001b[32m-  \033[0mID film: {self.__idMovie} \n" \
               f"\u001b[32m-  \033[0mID client:  {self.__idClient}\n" \
               f"\u001b[32m-  \033[0mData inceput: {self.__beginDate}\n" \
               f"\u001b[32m-  \033[0mData sfarsit:  {self.__endDate}\n"