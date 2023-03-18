from django.urls import path

from books.views import IndexView, ContactCreateView, BooksListView

app_name = 'books'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('shop/<str:category>-books/', BooksListView.as_view(), name='shop'),
    path('shop/<str:category>-books/<int:page>/', BooksListView.as_view(), name='paginator'),
    path('shop/view/<str:name>/', BooksListView.as_view(), name='view'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
]
