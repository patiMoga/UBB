from unittest import TestCase

from ro.ubb.store.exceptions.exceptions import FormatIdError, Validators, StringFormatError, EntityError, CNPFormatError


class TestValidators(TestCase):
    def setUp(self) -> None:
        pass

    def test_validate_movie(self):
        self.assertIsNone(Validators.validate_movie(1, 'abc', 'abc', 'abc'))
        with self.assertRaises(EntityError):
            Validators.validate_movie('a', '', '', '')

    def test_validate_client(self):
        self.assertIsNone(Validators.validate_client(1, 'T', 123))
        with self.assertRaises(EntityError):
            Validators.validate_client('a', '', 'b')

    def test_validate_rent(self):
        self.assertIsNone(Validators.validate_rent(1, 2, 3, 'asd', 'asd', 'asd'))
        with self.assertRaises(EntityError):
            Validators.validate_rent('1', '2', '3', '', '', '')

    def test_id_validator(self):
        self.assertIsNone(Validators.validate_id(1))
        with self.assertRaises(FormatIdError):
            Validators.validate_id('a')

    def test_CNP_validator(self):
        self.assertIsNone(Validators.validate_CNP(123))
        with self.assertRaises(CNPFormatError):
            Validators.validate_CNP('1a')

    def test_validate_string(self):
        self.assertIsNone(Validators.validate_string('abc'))
        with self.assertRaises(StringFormatError):
            Validators.validate_string('')

    def tearDown(self) -> None:
        pass