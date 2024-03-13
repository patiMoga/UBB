from unittest import TestCase

from domain.entities import Cafea
from repository.cafea_repository import Repository
from service.cafea_service import CafeaService


def test_add():
    cafea_repository = Repository()
    cafea_service = CafeaService(cafea_repository)

    cafea_service.add(1,"asd","qwe",12.7)

    assert (len(cafea_service.getAll()) == 1)

class Test(TestCase):
    def test_sort(self):
        cafea_repository = Repository()
        cafea_service = CafeaService(cafea_repository)

        cafea_service.add(1,"asd","wwe",12.7)
        cafea_service.add(2, "asd", "zer", 17)

        lista = cafea_service.getAll()

        cafea_service.sortare()
        self.assertEqual(lista, cafea_service.getAll())


