# Generated by Django 4.1.7 on 2023-02-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('auth', models.CharField(max_length=30)),
                ('cd_auth', models.CharField(max_length=30)),
                ('register_date', models.DateField()),
                ('borrowed', models.BooleanField(default=False)),
                ('borrowed_to_name', models.CharField(max_length=30)),
                ('borrowing_date', models.DateTimeField()),
                ('borrowing_return', models.DateTimeField()),
                ('duration', models.DateField()),
            ],
        ),
    ]