from unittest import TestCase

from ro.ubb.store.domain.rent import Rent


class TestRent(TestCase):
    def setUp(self):
        self.rent = Rent(1, 2, 3, "17/03/2023", "19/03/2023", "NO")

    def test_id(self):
        self.assertTrue(self.rent.id == 1, "ID rent trebuie sa fie 1")
        self.assertFalse(self.rent.id == 'a', "ID rent nu trebuie sa fie a")

    def test_id_movie(self):
        self.assertTrue(self.rent.idMovie == 2, "ID film trebuie sa fie 2")
        self.assertFalse(self.rent.idMovie == 'b', "ID film nu trebuie sa fie b")

    def test_id_client(self):
        self.assertTrue(self.rent.idClient == 3, "ID client trebuie sa fie 3")
        self.assertFalse(self.rent.idClient == 'c', "ID client nu trebuie sa fie c")

    def test_beginDate(self):
        self.assertTrue(self.rent.beginDate == '17/03/2023', "Data inceput trebuie sa fie '17/03/2023'")
        self.assertFalse(self.rent.beginDate == 17/3/2023, "Data inceput nu trebuie sa fie 17/3/2023")

    def test_endDate(self):
        self.assertTrue(self.rent.endDate == '19/03/2023', "Data sfarsit trebuie sa fie '19/03/2023'")
        self.assertFalse(self.rent.endDate == 19/3/2023, "Data sfarsit nu trebuie sa fie 19/3/2023")

    def test_retRent(self):
        self.assertTrue(self.rent.returnedRent == 'NO', "Returnat = 'NO'")
        self.assertFalse(self.rent.returnedRent == 123, "Returnat != 123")

    def test_id_set(self):
        self.rent.id = 2
        self.assertTrue(self.rent.id == 2, "ID rent trebuie sa fie 2")
        self.assertFalse(self.rent.id == 1, "ID rent nu trebuie sa fie 1")

    def test_id_movie_set(self):
        self.rent.idMovie = 3
        self.assertTrue(self.rent.idMovie == 3, "ID film trebuie sa fie 3")
        self.assertFalse(self.rent.idMovie == 2, "ID film nu trebuie sa fie 2")

    def test_id_client_set(self):
        self.rent.idClient = 4
        self.assertTrue(self.rent.idClient == 4, "ID client trebuie sa fie 4")
        self.assertFalse(self.rent.idClient == 3, "ID client nu trebuie sa fie 3")

    def test_beginDate_set(self):
        self.rent.beginDate = '19/03/2023'
        self.assertTrue(self.rent.beginDate == "19/03/2023", "Data inceput trebuie sa fie 19/03/2023")
        self.assertFalse(self.rent.endDate == '17/03/2023', "Data inceput nu trebuie sa fie 17/03/2023")

    def test_endDate_set(self):
        self.rent.endDate = '21/03/2023'
        self.assertTrue(self.rent.endDate == "21/03/2023", "Data sfarsit trebuie sa fie 21/03/2023")
        self.assertFalse(self.rent.endDate == '19/03/2023', "Data sfarsit nu trebuie sa fie 19/03/2023")

    def test_retRent_set(self):
        self.rent.returnedRent = "YES"
        self.assertTrue(self.rent.returnedRent == "YES", "Returnat = YES")
        self.assertFalse(self.rent.returnedRent == "NO", "Returnat != NO")

    def test_rent_str(self):
        self.assertTrue(self.rent.__str__() == '1 2 3 17/03/2023 19/03/2023 NO',
                        "Date rent trebuie sa fie '1 2 3 17/03/2023 19/03/2023 NO'")
        self.assertFalse(self.rent.__str__() == 'a 3 4 19/03/2023 21/03/2023 YES',
                         "Date rent nu trebuie sa fie 'a 3 4 19/03/2023 21/03/2023 YES'")

    def tearDown(self) -> None:
        pass
