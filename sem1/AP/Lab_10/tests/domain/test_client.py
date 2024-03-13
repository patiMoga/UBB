from unittest import TestCase

from ro.ubb.store.domain.client import Client


class TestClient(TestCase):
    def setUp(self):
        self.client = Client(1, "test1", 123)

    def test_id(self):
        self.assertTrue(self.client.id == 1, "ID client trebuie sa fie 1")
        self.assertFalse(self.client.id == 'a', "ID client nu trebuie sa fie a")

    def test_CNP(self):
        self.assertTrue(self.client.CNP == 123, "CNP client trebuie sa fie 123")
        self.assertFalse(self.client.CNP == 'asd', "CNP client nu trebuie sa fie asd")

    def test_name(self):
        self.assertTrue(self.client.name == 'test1', "Nume client trebuie sa fie test1")
        self.assertFalse(self.client.name == 123, "Nume client nu trebuie sa fie 123")

    def test_id_set(self):
        self.client.id = 2
        self.assertTrue(self.client.id == 2, "ID client trebuie sa fie 2")
        self.assertFalse(self.client.id == 1, "ID client nu trebuie sa fie 1")

    def test_name_set(self):
        self.client.name = 'test2'
        self.assertTrue(self.client.name == 'test2', "Nume client trebuie sa fie test2")
        self.assertFalse(self.client.name == 'test1', "Nume client nu trebuie sa fie test1")

    def test_CNP_set(self):
        self.client.CNP = 222
        self.assertTrue(self.client.CNP == 222, "CNP client trebuie sa fie 222")
        self.assertFalse(self.client.CNP == 123, "CNP client nu trebuie sa fie 123")

    def test_str(self):
        self.assertTrue(self.client.__str__() == '1 test1 123')
        self.assertFalse(self.client.__str__() == 'a 123 abc')

    def tearDown(self) -> None:
        pass