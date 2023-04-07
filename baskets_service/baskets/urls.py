from django.urls import path, include
from rest_framework import routers

from .views import BasketModelViewSet, TotalBasketAPIView

app_name = 'baskets'

router = routers.DefaultRouter()
router.register(r'current', BasketModelViewSet, basename='user_basket')

urlpatterns = [
    path('', include(router.urls), name='current'),
    path('total/', TotalBasketAPIView.as_view()),
]
