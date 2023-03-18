from django.urls import path

from books.views import IndexView, ContactListView

app_name = 'books'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactListView.as_view(), name='contact'),
]
