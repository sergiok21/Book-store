from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/orders/admin/', admin.site.urls),
    path('api/orders/', include('orders.urls')),
]
