from django.contrib import admin

# Register your models here.

from .models import Author, Publisher, Book


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ["last_name", "first_name"]
    ordering = ["last_name"]

class BookAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title"]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)


admin.site.register(Publisher)