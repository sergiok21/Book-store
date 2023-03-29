from django.urls import path, include
from rest_framework import routers

from .views import BasketAPIView, TotalBasketAPIView

app_name = 'baskets'

router = routers.DefaultRouter()
router.register(r'current', BasketAPIView, basename='user_basket')

urlpatterns = [
    path('', include(router.urls), name='current'),
    path('total/', TotalBasketAPIView.as_view()),
]
