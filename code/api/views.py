from django.shortcuts import render
from rest_framework import viewsets, mixins

from api.models import Book, Review
from api.serializers import BookSerializer, ReviewSerializer
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'id'

class Review(   mixins.CreateModelMixin,
                viewsets.GenericViewSet,
                ):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer