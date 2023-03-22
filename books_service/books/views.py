from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from books.models import Book, BookCategory, Preview, Recommendation, Partner, Contact, Message
from books.serializers import PreviewSerializer, BookSerializer, RecommendationSerializer, PartnerSerializer, \
    ContactSerializer, MessageSerializer, BookCategorySerializer
from common.views import PermissionMixin
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 6
    page_query_param = 'page_number'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'page_number': self.page.number,
            'results': data
        })


class BookAPIView(PermissionMixin, ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category', None)
        current = self.request.query_params.get('id', None)
        if category:
            if category == 'all':
                return queryset
            else:
                return queryset.filter(category__name__icontains=category)
        elif current:
            return queryset.filter(id=current)
        else:
            return queryset

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data={
            key: value for key, value in request.data.items() if value
        })
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        Preview.objects.filter(book__id=self.get_object().pk).update(**{
            key: value for key, value in request.data.items() if hasattr(Preview, key) if value
        })

        return Response(serializer.data, status=status.HTTP_200_OK)


class BookCategoryAPIView(PermissionMixin, ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    pagination_class = None


class PreviewAPIView(PermissionMixin, ModelViewSet):
    queryset = Preview.objects.all()
    serializer_class = PreviewSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class RecommendationAPIView(PermissionMixin, ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class PartnerAPIView(PermissionMixin, ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    pagination_class = None


class ContactAPIView(PermissionMixin, ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    pagination_class = None


class MessageAPIView(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = [SessionAuthentication]

    def get_permissions(self):
        if self.request.user.is_superuser:
            return [AllowAny()]
        return []

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if self.request.user.is_superuser:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        return Response({'detail': 'Enter your message.'}, status=status.HTTP_400_BAD_REQUEST)
