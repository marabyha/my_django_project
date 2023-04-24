from django.contrib import admin
from .models import Author, Genre, Book, BookInstance
admin.site.register(Genre)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


admin.site.register(Author, AuthorAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'id', 'cover')


@admin.register(BookInstance)
class UserAdmin(admin.ModelAdmin):
    list_display = ('book', 'user')
