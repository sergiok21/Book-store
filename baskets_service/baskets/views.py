import requests
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .authentication import CustomTokenAuthentication, CustomIsAuthenticated
from .models import Basket
from .serializers import BasketSerializer, TotalBasketSerializer


class BasketAPIView(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [CustomIsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.COOKIES.get('User')
        return queryset.filter(user_id=user)

    def list(self, request, *args, **kwargs):
        user = self.request.COOKIES.get('User')
        if not user:
            self.permission_classes = [IsAuthenticated]
            return Response({'detail': 'Where the user id?'}, status=status.HTTP_400_BAD_REQUEST)
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        try:
            book_id = request.data['book_id']
            user_id = request.data['user_id']
            message = request.data.get('message')

            product = requests.get(f'http://127.0.0.1:8001/api/books/all/{book_id}/')
            if product.status_code != status.HTTP_200_OK:
                return Response({'book_id': 'This product does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            obj, is_created = Basket.create_or_update(user_id=user_id, book_id=book_id, message=message)
            status_code = status.HTTP_201_CREATED if is_created else status.HTTP_200_OK
            serializer = self.get_serializer(obj)
            return Response(serializer.data, status=status_code)
        except KeyError:
            return Response({'book_id': 'Field "book_id" is required.', 'user_id': 'Field "user_id" is required.'},
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['delete'], url_path='delete')
    def delete_all(self, request):
        self.get_queryset().delete()
        return Response({'message': 'All records have been deleted.'}, status=status.HTTP_204_NO_CONTENT)


class TotalBasketAPIView(APIView):
    serializer_class = TotalBasketSerializer
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [CustomIsAuthenticated]

    def get(self, request):
        user_id = request.COOKIES.get('User')
        total_sum = Basket.objects.filter(user_id=user_id).total_sum()
        total_quantity = Basket.objects.filter(user_id=user_id).total_quantity()
        context = {'total_sum': total_sum, 'total_quantity': total_quantity}
        return Response(context, status=status.HTTP_200_OK)
