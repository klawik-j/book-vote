from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from api.models import Book

client = APIClient()


class ReviewEndpointTestCase(TestCase):
    def setUp(self):
        self.url = reverse('review-list')
        self.book = Book.objects.create(author='J.R.R. Tolkien', title='The Hobbit')

    def test_get_code(self):
        response = client.get(self.url)
        self.assertEqual(response.status_code, 405)

    def test_post_code(self):
        response = client.post( self.url,
                                {'book': self.book.id,
                                'review': '4'})
        self.assertEqual(response.status_code, 201)

    def test_post_wrong(self):
        response = client.post( self.url,
                                {'book': self.book.id,
                                'review': '6'})
        self.assertEqual(response.status_code, 400)

    def test_post_data(self):
        response = client.post( self.url,
                                {'book': self.book.id,
                                'review': '4'})
        self.assertIsNotNone(response.data['book'])
        self.assertIsNotNone(response.data['review'])