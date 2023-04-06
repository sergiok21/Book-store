from django.urls import path

from .views import IndexView, ContactCreateView, BooksListView, ReviewDetailView, ProfileView

app_name = 'books'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('shop/<str:category>-books/', BooksListView.as_view(), name='shop'),
    path('shop/<str:category>-books/page-<int:page>/', BooksListView.as_view(), name='paginator'),
    path('shop/review/book-<int:pk>/', ReviewDetailView.as_view(), name='review'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
