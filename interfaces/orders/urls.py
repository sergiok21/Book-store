from django.urls import path

from orders.views import OrdersTemplateView, CurrentOrderTemplateView

app_name = 'orders'

urlpatterns = [
    path('order/', OrdersTemplateView.as_view(), name='order'),
    path('order/<int:pk>/', CurrentOrderTemplateView.as_view(), name='current'),
]
