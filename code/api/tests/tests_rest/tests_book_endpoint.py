from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from api.models import Review, Book
from django.db.utils import IntegrityError

client = APIClient()

class BookEndpointTestCase(TestCase):
    def setUp(self):
        self.url = reverse('book-list')
        self.books = [
            Book(author='J.R.R. Tolkien', title='The Hobbit'),
            Book(author='Fyodor Dostoevsky', title='Crime and Punishment'),
            Book(author='Richard Phillips Feynman', title="Surely You're Joking, Mr. Feynman"),
            Book(author='Michio Kaku', title='Physics of the Impossible'),
            Book(author='Cixin Liu', title='The Three-Body Problem'),
        ]
        for book in self.books:
            book.save()
            Review.objects.create(book=book, review=2)

    def test_post_wrong_book(self):
        response = client.post( self.url,
                                {'author': 'Gimli',
                                'title': 'The Dwarf'})
        self.assertEqual(response.status_code, 400)
    
    def test_post_duplicate_book(self):
        response = client.post(self.url,
                    {'author': 'J.R.R. Tolkien',
                    'title': 'The Hobbit'})
        self.assertEqual(response.status_code, 400)

    def test_post_code(self):
        response = client.post( self.url,
                                {'author': 'Cixin Liu',
                                'title': "Death's End"})
        self.assertEqual(response.status_code, 201)

    def test_post_data(self):
        response = client.post( self.url,
                                {'author': 'Cixin Liu',
                                'title': "Death's End"})
        data = response.data
        self.assertIsNotNone(data['id'])
        self.assertEqual(data['author'], 'Cixin Liu')
        self.assertEqual(data['title'], "Death's End")

    def test_get_data(self):
        response = client.get(self.url)
        data = response.data
        self.assertEqual(len(self.books), len(data))
        self.assertCountEqual(data[0].keys(),
                             ['id', 'author', 'title', 'average_rating'])
        self.assertEqual(data[0]['average_rating'], '2.0')
        self.assertEqual(data[0]['author'], 'J.R.R. Tolkien')
        self.assertEqual(data[0]['title'], 'The Hobbit')

    def test_put_code(self):
        response = client.put(self.url)
        self.assertEqual(response.status_code, 405)

    def test_delete_code(self):
        response = client.delete(self.url)
        self.assertEqual(response.status_code, 405)