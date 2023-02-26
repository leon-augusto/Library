from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
from django.shortcuts import redirect
from hashlib import sha256


def login(request):
    if request.session.get('client'):
        return redirect('/books/home')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def valid_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    password = sha256(password.encode()).hexdigest()

    client = Client.objects.filter(email=email).filter(password=password)

    if len(client) == 0:
        return redirect('/auth/login/?status=1')
    elif len(client) > 0:
        request.session['client'] = client[0].id
        return redirect('/books/home')

    return HttpResponse(f'{email} {password}')


def logout(request):
    request.session.flush()
    return redirect('/auth/login/')


def register(request):
    if request.session.get('client'):
        return redirect('/books/home')
    status = request.GET.get('status')
    return render(request, 'register.html', {'status': status})


def valid_register(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')

    client = Client.objects.filter(email=email)

    if len(name.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/register/?status=1')

    if len(password) < 8:
        return redirect('/auth/register/?status=2')

    if len(client) > 0:
        return redirect('/auth/register/?status=3')

    try:
        password = sha256(password.encode()).hexdigest()
        client = Client(name=name, email=email, password=password)
        client.save()

        return redirect('/auth/register/?status=0')

    except:
        return redirect('/auth/register/?status=4')
