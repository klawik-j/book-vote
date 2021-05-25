from django.test import TestCase
from api.serializers import BookSerializer, ReviewSerializer
from api.models import Book, Review


class BookSerializerTestCase(TestCase):
    def setUp(self):
        self.book_attributes = {'author': 'J.R.R. Tolkien', 'title': 'The Hobbit'}
        self.book = Book.objects.create(**self.book_attributes)
        self.review = [
            Review.objects.create(book=self.book, review=n % 5) for n in range(0, 5)
        ]
        self.serializer = BookSerializer(instance=self.book)

    def test_contains_expexed_fields(self):
        self.assertCountEqual(
            self.serializer.data.keys(), ['id', 'author', 'title', 'average_rating']
        )

    def test_validation(self):
        self.book_attributes['author'] = 'Gimli'
        serializer = BookSerializer(data=self.book_attributes)
        self.assertFalse(serializer.is_valid())

    def test_average_rating(self):
        self.assertAlmostEqual(
            float(self.serializer.data['average_rating']),
            self.book.average_rating(),
            places=1,
        )


class ReviewSerializerTestCase(TestCase):
    def setUp(self):
        self.book = Book.objects.create(author='J.R.R. Tolkien', title='The Hobbit')
        self.review_data = {'book': self.book.id, 'review': 5}
        self.review = Review.objects.create(book=self.book, review=5)
        self.serializer = ReviewSerializer(instance=self.review)

    def test_contains_expexed_fields(self):
        self.assertCountEqual(self.serializer.data.keys(), ['id', 'book', 'review'])

    def test_validation(self):
        self.review_data['review'] = 6
        serializer = ReviewSerializer(data=self.review_data)
        self.assertFalse(serializer.is_valid())
