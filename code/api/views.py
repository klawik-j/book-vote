from django.shortcuts import render
from rest_framework import viewsets

from api.models import Book
from api.serializers import BookSerializer
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'id'