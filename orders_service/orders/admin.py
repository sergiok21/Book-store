from django.contrib import admin

from .models import Order


@admin.register(Order)
class BookAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'first_name', 'last_name']
    search_fields = ['order_number']
    search_help_text = 'Order number'
    readonly_fields = ['user_id', 'order_number', 'extra_data', 'created_timestamp']
