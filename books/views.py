from django.http import HttpResponse
from django.shortcuts import render, redirect

from books.models import Book, Category, Borrowing
from clients.models import Client


def home(request):
    if request.session.get('client'):
        client = Client.objects.get(id=request.session['client'])
        books = Book.objects.filter(client=client)
        return render(request, 'home.html', {'books': books})
    else:
        return redirect('/auth/login/?status=2')


def see_book(request, id):
    if request.session.get('client'):
        book = Book.objects.get(id=id)
        if request.session.get('client') == book.client.id:
            books_categories = Category.objects.filter(client_id=request.session.get('client'))
            borrowings = Borrowing.objects.filter(book=book)
            return render(request, 'see_book.html', {'book': book, 'books_categories': books_categories, 'borrowings': borrowings})
        else:
            return HttpResponse('This book is not your!')
    return redirect('/auth/login/?status=2')
