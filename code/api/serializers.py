from rest_framework import serializers
from api.models import Book, Review


class BookSerializer(serializers.ModelSerializer):
    average_rating = serializers.DecimalField(
        max_digits=2, decimal_places=1, read_only=True
    )

    class Meta:
        model = Book
        fields = [
            'id',
            'author',
            'title',
            'average_rating',
        ]
        lookup_field = 'id'
        extra_kwargs = {'url': {'lookup_field': 'id'}}

    def validate(self, attrs):
        instance = Book(**attrs)
        instance.clean()
        return attrs


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'book',
            'review',
        ]
