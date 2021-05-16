from django.shortcuts import render
from rest_framework import viewsets, mixins

from api.models import Book, Review
from api.serializers import BookSerializer, ReviewSerializer
# Create your views here.

class BookViewSet(  mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet,
                    ):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'id'

class ReviewViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet,
                    ):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class PopularBooksViewSet(  mixins.ListModelMixin,
                            viewsets.GenericViewSet,
                        ):
    queryset = Book.most_popular()
    serializer_class = BookSerializer