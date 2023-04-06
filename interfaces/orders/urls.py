from django.urls import path

from orders.views import OrdersTemplateView, CurrentOrderTemplateVIew

app_name = 'orders'

urlpatterns = [
    path('order/', OrdersTemplateView.as_view(), name='order'),
    path('order/<int:pk>/', CurrentOrderTemplateVIew.as_view(), name='current'),
]
