from django.urls import path

from books.views import IndexView

app_name = 'books'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
