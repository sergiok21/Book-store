from django.conf import settings
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('', lambda req: redirect('books/')),
    path('books/', include('books.urls', namespace='books')),
    path('users/', include('users.urls', namespace='users')),
    path('baskets/', include('baskets.urls', namespace='baskets')),
    path('orders/', include('orders.urls', namespace='orders')),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')),)
