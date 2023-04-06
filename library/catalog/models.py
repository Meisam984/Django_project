from django.db import models
from django.urls import reverse

import uuid

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f"{self.name}"

    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(to='Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=600)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    genre = models.ManyToManyField(to=Genre)
    language = models.ForeignKey(to='Language', on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey(to='Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    LOAN_STATUS = (
                    ('m', 'Maintenance'),
                    ('o', 'On Laon'),
                    ('a', 'Available'),
                    ('r', 'Reserved')
                  )
    
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m')
    class Meta:
        ordering = ['due_back']

    def __str__(self) -> str:
        return f"{self.id} ({self.book.title})"
    
class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name