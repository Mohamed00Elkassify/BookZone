from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list, name='books_list'),
    path('read/<int:book_id>', views.read_book, name='read_book'),
    path('bookmark/<int:book_id>', views.bookmark_book, name='bookmark_book'),
    path('bookmarked/', views.bookmarked_books, name='bookmarked_books'),
    path('remove/<int:book_id>', views.remove_bookmark, name='remove_bookmark'),
    #path('', views.download_book, name='download_book'),
]