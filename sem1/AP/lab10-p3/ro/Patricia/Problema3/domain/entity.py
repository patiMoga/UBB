class Entity:
    def __init__(self,id_entity):
        self.__id_entity=id_entity

    def get_id_entity(self):
        return self.__id_entity

    def set_id_entity(self,value):
        self.__id_entity=value