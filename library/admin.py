from django.contrib import admin
from .models import Book, Author, BookingBook, Comments


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "price", "count", "create_date")
    list_display_links = ("title", "description", "price", "count", "create_date")
    search_fields = ("id", "title")
    ordering = ("title",)


admin.site.register(Author)
admin.site.register(BookingBook)
admin.site.register(Comments)
