from unittest import TestCase

from ro.ubb.store.domain.dto import ClientAssemble, ClientFQAssemble, ClientDTOAssemble


class TestDTO(TestCase):
    def setUp(self):
        self.dto = ClientAssemble(1, 'abc')
        self.dto_fr = ClientFQAssemble('abc', 1)

    def test_dto(self):
        self.assertTrue(self.dto.id == 1)
        self.assertFalse(self.dto.id == 'a')

        self.assertTrue(self.dto.name == 'abc')
        self.assertFalse(self.dto.name == '')

    def test_dto_frq(self):
        self.assertTrue(self.dto_fr.freq == 1)
        self.assertFalse(self.dto_fr.freq == 'a')

        self.assertTrue(self.dto_fr.name == 'abc')
        self.assertFalse(self.dto_fr.name == '')

    def test_create_client_dto(self):
        dto = ClientDTOAssemble.create_client_dto(1, 'abc')
        self.assertTrue(isinstance(dto, ClientAssemble))
        self.assertFalse(isinstance(dto, ClientFQAssemble))
        self.assertTrue(dto.id == 1)
        self.assertFalse(dto.id == 'a')
        self.assertTrue(dto.name == 'abc')
        self.assertFalse(dto.name == '')

    def test_create_client_freq_dto(self):
        dto = ClientDTOAssemble.create_client_freq_dto('abc', 1)
        self.assertTrue(isinstance(dto, ClientFQAssemble))
        self.assertFalse(isinstance(dto, ClientAssemble))
        self.assertTrue(dto.freq == 1)
        self.assertFalse(dto.freq == 'a')
        self.assertTrue(dto.name == 'abc')
        self.assertFalse(dto.name == '')