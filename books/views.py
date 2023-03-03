from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q

from books.models import Book, Category, Borrowing
from clients.models import Client
from .forms import BookForm, CategoryForm, BorrowingForm
from datetime import datetime


def home(request):
    if request.session.get('client'):
        client = Client.objects.get(id=request.session['client'])
        books = Book.objects.filter(client=client)

        form_book, form_category, form_borrowing = BookForm(), CategoryForm(), BorrowingForm()

        form_category.fields['client'].initial = request.session['client']
        form_book.fields['client'].initial = request.session['client']

        form_book.fields['category'].queryset = Category.objects.filter(client=client)
        form_borrowing.fields['book'].queryset = Book.objects.filter(client=client, borrowed=False)

        borrowed_books = Book.objects.filter(client=client, borrowed=True)

        return render(request, 'home.html', {'books': books,
                                             'client_logged_in': request.session.get('client'),
                                             'form_book': form_book,
                                             'form_category': form_category,
                                             'form_borrowing': form_borrowing,
                                             'borrowed_books': borrowed_books})
    else:
        return redirect('/auth/login/?status=2')


def see_book(request, id):
    if request.session.get('client'):
        client = Client.objects.get(id=request.session['client'])
        book = Book.objects.get(id=id)

        form_book, form_category, form_borrowing = BookForm(), CategoryForm(), BorrowingForm()

        form_category.fields['client'].initial = request.session['client']
        form_book.fields['client'].initial = request.session['client']

        form_book.fields['category'].queryset = Category.objects.filter(client=client)
        form_borrowing.fields['book'].queryset = Book.objects.filter(client=client, borrowed=False)

        borrowed_books = Book.objects.filter(client=client, borrowed=True)

        if request.session.get('client') == book.client.id:
            books_categories = Category.objects.filter(client_id=request.session.get('client'))
            borrowings = Borrowing.objects.filter(book=book)
            return render(request, 'see_book.html', {'book': book,
                                                     'books_categories': books_categories,
                                                     'borrowings': borrowings,
                                                     'client_logged_in': request.session.get('client'),
                                                     'form_book': form_book,
                                                     'form_category': form_category,
                                                     'form_borrowing': form_borrowing,
                                                     'borrowed_books': borrowed_books,
                                                     'id_book': id})
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


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/home')
        else:
            return HttpResponse('Invalid Datas')


def create_borrowing(request):
    if request.method == 'POST':
        form = BorrowingForm(request.POST)
        borrowed_book_id = request.POST.get('book')

        if form.is_valid():
            form.save()

            book = Book.objects.get(id=borrowed_book_id)
            book.borrowed = True
            book.save()
            return redirect('/books/home')
        else:
            return HttpResponse('Invalid Datas')


def return_of_book(request):
    id = request.POST.get('book_id')
    book = Book.objects.get(id=id)
    book.borrowed = False
    book.save()

    borrowing = Borrowing.objects.get(Q(book=book) & Q(book_return=None))
    borrowing.book_return = datetime.now()
    borrowing.save()
    return HttpResponse('Returned Book')


def remove_book(request, id):
    Book.objects.get(id=id).delete()
    return redirect('/books/home')
