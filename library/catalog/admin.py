from django.contrib import admin
from catalog.models import Book, Author, BookInstance, Genre, Language

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)