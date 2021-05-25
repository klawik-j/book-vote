from django.test import TestCase
from django.core.exceptions import ValidationError
from api.models import Book, Review


class ReviewModelTestCase(TestCase):
    def setUp(self):
        self.book = Book(author='J.R.R. Tolkien', title='The Hobbit')
        self.book.save()
        self.review = Review(book=self.book, review=5)

    def test_review_creation(self):
        self.review.save()
        self.assertIsNotNone(self.review.id)

    def test_review_low_validation(self):
        with self.assertRaises(ValidationError):
            self.review.review = -1
            self.review.full_clean()

    def test_review_high_validation(self):
        with self.assertRaises(ValidationError):
            self.review.review = 6
            self.review.full_clean()
