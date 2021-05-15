from rest_framework import serializers
from api.models import Book


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = [  'id',
                    'author',
                     'title',
                     ]
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }
    
    def validate(self, attrs):
        instance = Book(**attrs)
        instance.clean()
        return attrs
