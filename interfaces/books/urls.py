from django.urls import path

from .views import IndexTemplateView, ContactFormView, BooksTemplateView, ReviewTemplateView, ProfileFormView

app_name = 'books'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('shop/<str:category>-books/', BooksTemplateView.as_view(), name='shop'),
    path('shop/<str:category>-books/page-<int:page>/', BooksTemplateView.as_view(), name='paginator'),
    path('shop/review/book-<int:pk>/', ReviewTemplateView.as_view(), name='review'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('profile/', ProfileFormView.as_view(), name='profile'),
]
