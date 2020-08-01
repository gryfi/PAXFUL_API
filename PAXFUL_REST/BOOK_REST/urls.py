from BOOK_REST import views
from django.urls import path


urlpatterns = [

path('/books/', views.BookList.as_view(),name='booklist'),
path('/books/<int:pk>/', views.BookDetail.as_view(),name='bookdetail'),
]
