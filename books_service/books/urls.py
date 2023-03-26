from django.urls import path, include
from rest_framework import routers

from .views import PreviewAPIView, RecommendationAPIView, PartnerAPIView, ContactAPIView, MessageAPIView,\
    BookAPIView, BookCategoryAPIView

app_name = 'books'

router = routers.DefaultRouter()
router.register(r'all', BookAPIView)
router.register(r'categories', BookCategoryAPIView)
router.register(r'previews', PreviewAPIView)
router.register(r'recommendations', RecommendationAPIView)
router.register(r'partners', PartnerAPIView)
router.register(r'contacts', ContactAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('messages/', MessageAPIView.as_view(), name='message')
]
