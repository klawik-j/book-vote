import random

from django.test import TestCase
from django.core.exceptions import ValidationError
from api.models import Book, Review

class BookModelTestCase(TestCase):
    def setUp(self):
        self.book = Book(author='J.R.R. Tolkien', title='The Hobbit')

    def test_book_creation(self):
        self.book.full_clean()
        self.book.save()
        self.assertIsNotNone(self.book.id)

    def test_book_author_validation(self):
        with self.assertRaises(ValidationError):
            self.book.author = "Jakub Klawikowski"
            self.book.full_clean()

    def test_book_title_validation(self):
        with self.assertRaises(ValidationError):
            self.book.title = "Not a book tiitle"
            self.book.full_clean()

class BookReviewTestCase(TestCase):
    def setUp(self):
        #Create books list and save it
        self.books = [
            Book(author='J.R.R. Tolkien', title='The Hobbit'),
            Book(author='Fyodor Dostoevsky', title='Crime and Punishment'),
            Book(author='Richard Phillips Feynman', title="Surely You're Joking, Mr. Feynman"),
            Book(author='Michio Kaku', title='Physics of the Impossible'),
            Book(author='Cixin Liu', title='The Three-Body Problem'),
        ]
        [book.save() for book in self.books]

        #Create a dictionary contain n number of random reviews bound to book
        self.reviews = dict()
        for n, book in enumerate(self.books, start=1):
            self.reviews[str(book)] = {
                'avg': 0,
                'reviews': list(),
                'number_of_reviews':int()
            }
            self.reviews[str(book)]['number_of_reviews'] = n
            for _ in range(n):
                rate = random.randrange(0, 5)
                review = Review(book=book, review=rate)
                review.save()
                self.reviews[str(book)]['reviews'].append(review)
                self.reviews[str(book)]['avg'] += rate
            self.reviews[str(book)]['avg'] /= n

    def test_average_rating(self):
        for book in self.books:
            self.assertEqual(book.average_rating(), 
                             self.reviews[str(book)]['avg'])

    def test_average_no_reviews(self):
        book = Book(author='Cixin Liu', title="Death's End")
        book.save()
        self.assertIsNone(book.average_rating())

    def test_review_count(self):
        for book in self.books:
            self.assertEqual(book.number_of_reviews(), 
                             self.reviews[str(book)]['number_of_reviews'])

    def test_popular(self):
        popular = Book.most_popular()
        self.assertEqual(len(popular), 5)
        self.assertListEqual(list(popular), list(reversed(self.books)))
        self.assertEqual(type(popular), type(Book.objects.all()))

    
