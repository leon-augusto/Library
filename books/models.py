from django.db import models
from datetime import date


class Book(models.Model):
    name = models.CharField(max_length=100)
    auth = models.CharField(max_length=30)
    cd_auth = models.CharField(max_length=30, blank=True, null=True)
    register_date = models.DateField(default=date.today)
    borrowed = models.BooleanField(default=False)
    borrowed_to_name = models.CharField(max_length=30, blank=True, null=True)
    borrowing_date = models.DateTimeField(blank=True, null=True)
    borrowing_return = models.DateTimeField(blank=True, null=True)
    duration = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}, by {self.auth}'
