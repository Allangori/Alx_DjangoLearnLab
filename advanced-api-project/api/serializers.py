from rest_framework import serializers
from datetime import date
from .models import Book, Author

class BookSerializers(serializers.ModelSerializer) :
    class Meta:
        model = Book
        #fields = '__all__'
        fields = ['title', 'publication_year', 'author']
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError('Publication year cannot be in the future.')
        return value

class AuthorSerializers(serializers.ModelField):
    books = BookSerializers(many = True, read_only = True)
    class Meta:
        model = Author
        fields = ['name', 'books']