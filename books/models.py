from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField("ISBN", max_length=13, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
