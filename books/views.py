from django.http import HttpResponse
from django.shortcuts import render, redirect

from books.models import Book, Category, Borrowing
from clients.models import Client
from .forms import BookForm


def home(request):
    if request.session.get('client'):
        client = Client.objects.get(id=request.session['client'])
        books = Book.objects.filter(client=client)
        form = BookForm()
        form.fields['client'].initial = request.session['client']
        form.fields['category'].queryset = Category.objects.filter(client=client)
        return render(request, 'home.html', {'books': books,
                                             'client_logged_in': request.session.get('client'),
                                             'form': form})
    else:
        return redirect('/auth/login/?status=2')


def see_book(request, id):
    if request.session.get('client'):
        client = Client.objects.get(id=request.session['client'])
        book = Book.objects.get(id=id)
        form = BookForm()
        form.fields['client'].initial = request.session['client']
        form.fields['category'].queryset = Category.objects.filter(client=client)
        if request.session.get('client') == book.client.id:
            books_categories = Category.objects.filter(client_id=request.session.get('client'))
            borrowings = Borrowing.objects.filter(book=book)
            return render(request, 'see_book.html', {'book': book,
                                                     'books_categories': books_categories,
                                                     'borrowings': borrowings,
                                                     'client_logged_in': request.session.get('client'),
                                                     'form': form})
        else:
            return HttpResponse('This book is not your!')
    return redirect('/auth/login/?status=2')


def register_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/home')
        else:
            return HttpResponse('Invalid Datas')
