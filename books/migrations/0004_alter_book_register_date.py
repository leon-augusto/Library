# Generated by Django 4.1.7 on 2023-02-17 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_register_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='register_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
