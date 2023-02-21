from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.name
