import random

from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from api.models import Book, Review

client = APIClient()


class PopularEndpointTestCase(TestCase):
    def setUp(self):
        self.url = reverse('popular-list')
        # Create books list and save it
        self.books = [
            Book(author='J.R.R. Tolkien', title='The Hobbit'),
            Book(author='Fyodor Dostoevsky', title='Crime and Punishment'),
            Book(author='Richard Phillips Feynman', title="Surely You're Joking, Mr. Feynman"),
            Book(author='Michio Kaku', title='Physics of the Impossible'),
            Book(author='Cixin Liu', title='The Three-Body Problem'),
        ]
        [book.save() for book in self.books]

        # Create a dictionary contain n number of random reviews bound to book
        self.reviews = dict()
        for n, book in enumerate(self.books, start=1):
            self.reviews[str(book)] = {
                'avg': 0,
                'reviews': list(),
                'number_of_reviews': int(),
            }
            self.reviews[str(book)]['number_of_reviews'] = n
            for _ in range(n):
                rate = random.randrange(0, 5)
                review = Review(book=book, review=rate)
                review.save()
                self.reviews[str(book)]['reviews'].append(review)
                self.reviews[str(book)]['avg'] += rate
            self.reviews[str(book)]['avg'] /= n

    def test_get_code(self):
        response = client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_get_data(self):
        response = client.get(self.url)
        data = response.data
        self.assertEqual(len(data), 5)
        for (response_book, actual_book) in zip(data, list(reversed(self.books))):
            self.assertEqual(response_book['id'], actual_book.id)
