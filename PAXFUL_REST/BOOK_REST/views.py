from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from BOOK_REST.models import Book
from BOOK_REST.serializers import BookSerializer
from BOOK_REST.serializers import BookDetailSerializer
from django.http import HttpResponse, Http404, HttpResponseBadRequest
import sys


class BookList(APIView):
    """
    Retrieve the entire list of books
    """
    def get_list(self):
        books = Book.objects.all()
        return books
    def get(self, request):
        try:
            books = self.get_list()
            serializer = BookSerializer(books,many=True)
            if (len(books)!=0):
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
        except:
            print ("Unexpected error:", sys.exc_info()[0])


class BookDetail(APIView):
    """
    Retrieve a product instance with details
    """
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404
        except:
            print ("An Unexpected error occured:", sys.exc_info()[0])

    def get(self, request, pk, format=None):
        book1 = self.get_object(pk)
        serializer = BookDetailSerializer(book1)
        return Response(serializer.data)
