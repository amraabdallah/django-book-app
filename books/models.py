from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ForeignKey('Author', on_delete=models.CASCADE)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    age_ratings = (
        ('Childrens', 'Under 8'),
        ('Young Adult', '8 - 15'),
        ('Adults Only', '15 and up'),
    )
    appropriate = models.CharField(
        max_length=15, choices=age_ratings, default='adults only')

    image = models.ImageField(upload_to='books/static/books/images/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('books:detail', kwargs={'id': self.id})



class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def books(self):
        return self.book_set.all()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
