# books/admin.py
from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Book


@admin.register(Book)
class BookAdmin(ModelAdmin):
    list_display = ("title", "subtitle", "author", "isbn")  # ✅ matches your model
    search_fields = ("title", "subtitle", "author", "isbn")  # adds a search box
