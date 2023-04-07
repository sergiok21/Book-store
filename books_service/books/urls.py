from django.urls import path, include
from rest_framework import routers

from .views import PreviewModelViewSet, RecommendationModelViewSet, PartnerModelViewSet, ContactModelViewSet, MessageModelViewSet,\
    BookModelViewSet, BookCategoryModelViewSet

app_name = 'books'

router = routers.DefaultRouter()
router.register(r'all', BookModelViewSet)
router.register(r'categories', BookCategoryModelViewSet)
router.register(r'previews', PreviewModelViewSet)
router.register(r'recommendations', RecommendationModelViewSet)
router.register(r'partners', PartnerModelViewSet)
router.register(r'contacts', ContactModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('messages/', MessageModelViewSet.as_view(), name='message')
]
