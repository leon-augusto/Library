from django.db import models
from datetime import date
from clients.models import Client


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    auth = models.CharField(max_length=30)
    cd_auth = models.CharField(max_length=30, blank=True, null=True)
    register_date = models.DateField(default=date.today)
    borrowed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Borrowing(models.Model):
    responsible = models.ForeignKey(Client, on_delete=models.DO_NOTHING, blank=True, null=True)
    anonymous_responsible = models.CharField(max_length=30, blank=True, null=True)
    borrowing_date = models.DateField(blank=True, null=True)
    book_return = models.DateField(blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f'{self.responsible} | {self.book}'
