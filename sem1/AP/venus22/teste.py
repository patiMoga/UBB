import unittest
from domain.avion import Avion
from repository.repository import RepoAvioane
class Teste(unittest.TestCase):
    def chestii_domain(self):
        avion = Avion(0, "DC234", 2343)
        with self.assertRaises(ValueError):
            avion1=Avion("abc","SC234",2345)
        with self.assertRaises(ValueError):
            avion1 = Avion(-1, "SC234", 2345)
    def chestii_repo(self):
        avion=Avion(0,"DC234",2343)
        repo=RepoAvioane()
        repo.add_avi(avion)
        assert(len(repo.avioane)==1)
        avion2=Avion(0,"DI234",2345)
        with self.assertRaises(ValueError):
            repo.add_avi(avion2)




