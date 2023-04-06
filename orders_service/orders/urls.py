from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import OrderAPIView

app_name = 'orders'

router = DefaultRouter()
router.register(r'current', OrderAPIView)

urlpatterns = [
    path('', include(router.urls), name='current'),
]
