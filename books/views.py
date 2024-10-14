from django.shortcuts import render, redirect, get_object_or_404
from .models import Books
# Create your views here.

def books_list(request):
    books = Books.objects.all()
    return render(request, 'books/books_list.html', {'books' : books})

def read_book(request):
    pass

def bookmark_book(Request):
    pass

def bookmarked_books(request):
    pass

def download_book(request):
    pass

def remove_bookmark(request):
    pass