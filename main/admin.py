from django.contrib import admin

from .models import Book, Author, BookAndAuthor


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class BookAdmin(admin.ModelAdmin):
    pass
@admin.register(BookAndAuthor)
class BookAndAuthorAdmin(admin.ModelAdmin):
    pass