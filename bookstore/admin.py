from django.contrib import admin
from bookstore.models import Book, Author


# Register your models here.
class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub', 'prices', 'market_prices']


class AuthorManager(admin.ModelAdmin):
    list_display = ['name', 'age', 'email']


admin.site.register(Book, BookManager)
admin.site.register(Author, AuthorManager)
