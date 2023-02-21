from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    if request.session.get('client'):
        return HttpResponse('olá')
    else:
        return redirect('/auth/login/?status=2')
