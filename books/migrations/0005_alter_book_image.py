# Generated by Django 4.0.4 on 2022-04-20 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_remove_book_in_print_book_appropriate_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
