from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Books
import requests
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

def download_book(request, book_id):
    # get the book or return a 404 if not found
    book = get_object_or_404(Books, id=book_id)
    # Check if the book has a PDF link
    if not book.pdf_link:
        raise Http404("No  PDF link available.")
    # Download the PDF file from the link
    response = requests.get(book.pdf_link)
    # If the download was successful, server the file
    if response.status_code == 200:
        # Set the filename for download
        filename = f"{book.title}.pdf"
        # Create the HTTP response with the PDF content
        http_response = HttpResponse(response.content, content_type='application/pdf')
        http_response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return http_response