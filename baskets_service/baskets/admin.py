from django.contrib import admin

from .models import Basket


@admin.register(Basket)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'message']
    fields = ['book_id', 'user_id', 'name', 'price', 'quantity', 'message', 'created_timestamp']
    search_fields = ['name', 'price', 'user_id', 'message']
    search_help_text = 'Name | Price | User ID | Message'
    ordering = ['name']
    readonly_fields = ['name', 'price', 'quantity', 'message', 'created_timestamp']
