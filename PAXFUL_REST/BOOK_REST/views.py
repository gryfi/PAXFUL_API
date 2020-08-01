from rest_framework.views import APIView
from rest_framework.response import Response
from BOOK_REST.models import Book
from BOOK_REST.serializers import BookSerializer
from BOOK_REST.serializers import BookDetailSerializer
import sys


class BookList(APIView):
    """
    Retrieve the entire list of books
    """
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)


class BookDetail(APIView):
    """
    Retrieve a product instance with details
    """
    def get(self, request, pk, format=None):
        book1 = Book.objects.get(pk=pk)
        serializer = BookDetailSerializer(book1)
        return Response(serializer.data)
