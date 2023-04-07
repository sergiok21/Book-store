from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import OrderModelViewSet

app_name = 'orders'

router = DefaultRouter()
router.register(r'current', OrderModelViewSet)

urlpatterns = [
    path('', include(router.urls), name='current'),
]
