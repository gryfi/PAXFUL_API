from django.test import TestCase
from BOOK_REST.models import Book,Author
from django.urls import reverse,resolve
from BOOK_REST.views import BookList,BookDetail
from rest_framework.test import APITestCase
from rest_framework import status
from BOOK_REST.serializers import BookSerializer


"""
# Tests for checking for data in API response
"""

"""
    1. Test for list of books API response
    2. Test for concrete BookDetail retrival of Book by id

"""
class RetrievalSuccess(TestCase):
    def setUp(self):
        book_name1 = 'Anna Karenina'
        book_name2 = 'War and Peace'
        author_name = "Leo Tolstoy"
        author = Author.objects.get_or_create(name=author_name)[0]
        Book.objects.get_or_create(title=book_name1, author=author)
        Book.objects.get_or_create(title=book_name2,author=author)

    def test_booklist_retrieval_success_CorrectListSize(self):
        url = reverse('booklist')
        response = self.client.get(url)
        self.assertEquals(response.status_code,status.HTTP_200_OK)
        self.assertEquals(len(response.data),2)


    def test_bookdetail_retrieval_concrete_success(self):
        url = reverse('bookdetail',kwargs={"pk":1})
        response = self.client.get(url)
        self.assertEquals(response.data['title'],'Anna Karenina')
        self.assertEquals(response.data['id'],1)
        self.assertEquals(response.data['author']['name'],"Leo Tolstoy")
        self.assertEquals(response.status_code,status.HTTP_200_OK)



"""
    Tests with empty Database

    1.Test for empty list BookList response with a status code of 204

    2.Test for "detail": "Not found." BookDetail Response with status 404

"""
class RetrievalFailure_OR_NoContent(TestCase):
    def setUp(self):
        pass

    def test_bookdetail_retrieval_failure(self):
        url = reverse('bookdetail',kwargs={"pk":1})
        response = self.client.get(url)
        self.assertEquals(response.status_code,status.HTTP_404_NOT_FOUND)

    def test_booklist_retrieval_NoContent(self):
        url = reverse('booklist')
        response = self.client.get(url)
        self.assertEquals(response.status_code,status.HTTP_204_NO_CONTENT)
