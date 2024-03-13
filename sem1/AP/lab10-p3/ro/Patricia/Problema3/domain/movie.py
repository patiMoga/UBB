from ro.Patricia.Problema3.domain.entity import Entity


class Movie(Entity):
    def __init__(self, idMovie, title, description, genre):
        Entity.__init__(self,idMovie)
        self.__title = title
        self.__description = description
        self.__genre = genre

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def getDescription(self):
        return self.__description

    def setDescription(self, description):
        self.__description = description

    def getGenre(self):
        return self.__genre

    def setGenre(self, genre):
        self.__genre = genre

    def file_format(self):
        e = self.__str__()
        e = e.replace("[32m|  [0m", "")
        e = e.replace("ID: ", "")
        e = e.replace("Titlu:  ", "")
        e = e.replace("Gen:", "")
        e = e.replace("Descriere: ", "")
        e = e.replace("\n", "")
        return e


    def __str__(self):
        return f"\u001b[32m-  \033[0mID: {Entity.get_id_entity(self)} \n" \
               f"\u001b[32m-  \033[0mTitlu:  {self.__title}\n" \
               f"\u001b[32m-  \033[0mGen: {self.__genre}\n" \
               f"\u001b[32m-  \033[0mDescriere:  {self.__description}\n"


