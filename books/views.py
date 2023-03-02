from django.http import HttpResponse
from django.shortcuts import render, redirect

from books.models import Book, Category, Borrowing
from clients.models import Client
from .forms import BookForm, CategoryForm, BorrowingForm


def home(request):
    if request.session.get('client'):
        client = Client.objects.get(id=request.session['client'])
        books = Book.objects.filter(client=client)

        form_book, form_category, form_borrowing = BookForm(), CategoryForm(), BorrowingForm()

        form_category.fields['client'].initial = request.session['client']
        form_book.fields['client'].initial = request.session['client']

        form_book.fields['category'].queryset = Category.objects.filter(client=client)
        form_borrowing.fields['book'].queryset = Book.objects.filter(client=client)

        return render(request, 'home.html', {'books': books,
                                             'client_logged_in': request.session.get('client'),
                                             'form_book': form_book,
                                             'form_category': form_category,
                                             'form_borrowing': form_borrowing})
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
        form_borrowing.fields['book'].queryset = Book.objects.filter(client=client)

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
        if form.is_valid():
            form.save()
            return redirect('/books/home')
        else:
            return HttpResponse('Invalid Datas')


def remove_book(request, id):
    Book.objects.get(id=id).delete()
    return redirect('/books/home')
