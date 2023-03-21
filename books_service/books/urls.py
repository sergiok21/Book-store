from django.contrib.auth.views import LogoutView
from django.urls import path

from books.views import IndexView, ContactCreateView, BooksListView, ReviewDetailView

app_name = 'books'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('shop/<str:category>-books/', BooksListView.as_view(), name='shop'),
    path('shop/<str:category>-books/<int:page>/', BooksListView.as_view(), name='paginator'),
    path('shop/review/<int:pk>/', ReviewDetailView.as_view(), name='review'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('api/logout/', LogoutView.as_view(), name='logout')
]
