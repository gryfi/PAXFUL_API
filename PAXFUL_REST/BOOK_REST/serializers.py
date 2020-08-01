from rest_framework import serializers
from BOOK_REST.models import Book,Author
"""
# serializers for our Models to provide API Response in  JSON in
    accordance with standdards of rest_framework
"""

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id','title']

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id','name']


class BookDetailSerializer(serializers.ModelSerializer):
    """
    # In order to provide full author object to BookDetailSerializer
        we provide the BookDetailSerializer with
        AuthorSerializer as below in line 26
    """
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Book
        fields = ("id","title","author")
