from django.test import SimpleTestCase
from django.urls import reverse,resolve
from BOOK_REST import views
from BOOK_REST.views import BookList,BookDetail


"""
# Test for checking if corresponding response functions/classes
    are returned when we call the given APIs.
"""

class TestUrls(SimpleTestCase):

    def test_booklist_url_resolved(self):
        url = reverse('booklist')
        self.assertEquals(resolve(url).func.view_class,BookList)

    def test_bookdetail_url_resolved(self):
        url = reverse('bookdetail',kwargs={"pk":1})
        self.assertEquals(resolve(url).func.view_class,BookDetail)
