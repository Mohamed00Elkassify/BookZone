from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list, name='books_list'),
    #path('', views.read_book, name='read_book'),
    #path('', views.bookmark_book, name='bookmark_book'),
    #path('', views.bookmarked_books, name='bookmarked_books'),
    #path('', views.download_book, name='download_book'),
    #path('', views.remove_bookmark, name='remove_bookmark'),
]