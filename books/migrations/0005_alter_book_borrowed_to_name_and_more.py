# Generated by Django 4.1.7 on 2023-02-17 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_register_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='borrowed_to_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='borrowing_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='borrowing_return',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='cd_auth',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='duration',
            field=models.DateField(blank=True, null=True),
        ),
    ]