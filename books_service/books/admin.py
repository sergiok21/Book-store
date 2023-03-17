from django.contrib import admin

from books.models import Book, BookCategory, Preview, Recommendation


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category']
    fields = ['name', 'description', ('price', 'quantity'), 'image', 'category']
    readonly_fields = ['description']
    search_fields = ['name', 'price']
    search_help_text = 'Name | Price'
    ordering = ['name']


@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name', 'description']
    search_fields = ['name']
    search_help_text = 'Name'


@admin.register(Preview)
class PreviewAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['book']

    def save_model(self, request, obj, form, change):
        obj.name = obj.book.name
        obj.description = obj.book.description
        obj.save()


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['book']

    def save_model(self, request, obj, form, change):
        obj.name = obj.book.name
        obj.description = obj.book.description
        obj.save()
