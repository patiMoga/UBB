class Repository:
    def __init__(self):
        self.__all_cofee = {}

    def addCofee(self, cofee):
        if self.getById(cofee.getId()) is not None:
            raise ValueError("Id deja existent")

        self.__all_cofee[cofee.getId()] = cofee


    def getById(self, id):
        if id in self.__all_cofee:
            return self.__all_cofee[id]

        return None

    def getAll(self):
        return list(self.__all_cofee.values())

