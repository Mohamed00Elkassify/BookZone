from django.shortcuts import render, redirect, get_object_or_404
from .models import Books
# Create your views here.

def books_list(request):
    books = Books.objects.all()
    return render(request, 'books/books_list.html', {'books' : books})

def read_book(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    return render(request, 'books/read_book.html', {'book' : book})

def bookmark_book(Request, book_id):
    book = get_object_or_404(Books, id=book_id)
    book.bookmarked = True 
    book.save()
    return redirect('books_list')

def bookmarked_books(request):
    bookmarked_books = Books.objects.filter(bookmarked=True)
    return render(request, 'books/bookmarked_books.html', {'bookmarked_books' : bookmarked_books})

def remove_bookmark(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    book.bookmarked = False
    book.save()
    return redirect('bookmarked_books')

def download_book(request):
    pass