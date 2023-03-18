from django.contrib import admin

from books.models import Book, BookCategory, Preview, Recommendation, Partner, Message, Contact


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    fields = ['name', 'description', ('price', 'quantity'), 'image', 'category']
    search_fields = ['name', 'price']
    search_help_text = 'Name | Price'
    ordering = ['name']


@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__']
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
        obj.image = obj.book.image
        obj.save()


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['book']

    def save_model(self, request, obj, form, change):
        obj.name = obj.book.name
        obj.description = obj.book.description
        obj.price = obj.book.price
        obj.image = obj.book.image
        obj.save()


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name', 'image']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    fields = [('email', 'phone'), ('country', 'city'), ('street', 'house', 'corps', 'postal')]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    fields = [('name', 'email'), 'message']
    readonly_fields = [field.name for field in Message._meta.get_fields()]

    def has_add_permission(self, request):
        return False
