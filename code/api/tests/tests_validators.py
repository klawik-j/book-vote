from django.test import TestCase
from django.core.exceptions import ValidationError
from api.validators import validate_book


class BookValidatorTestCase(TestCase):
    def setUp(self):
        self.real_book = {'author': 'J.R.R. Tolkien', 'title': 'The Hobbit'}
        self.fake_book = {'author': 'Gimli', 'title': 'The Dwarf'}

    def test_correct_book(self):
        result = validate_book(**self.real_book)
        self.assertEqual(result[0], self.real_book["author"])
        self.assertEqual(result[1], self.real_book["title"])

    def test_incorrect_book(self):
        errormsg = "Book {title} written by {author} has never benn published".format(
            author=self.fake_book["author"], title=self.fake_book["title"]
        )
        with self.assertRaisesMessage(ValidationError, errormsg):
            validate_book(**self.fake_book)
