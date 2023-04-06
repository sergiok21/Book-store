from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .authentication import CustomTokenAuthentication, CustomIsAuthenticated
from .models import Order
from .serializers import OrderSerializer


class OrderAPIView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [CustomIsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.COOKIES.get('User')
        return queryset.filter(user_id=user_id)

    def create(self, request, *args, **kwargs):
        try:
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            email = request.data['email']
            phone = request.data['phone']
            address = request.data['address']
            message = request.data['message']
            extra_data = request.data['extra_data']
            total_sum = float(request.data['total_sum'])
            total_quantity = int(request.data['total_quantity'])
            user_id = self.request.COOKIES.get('User')
            Order.objects.create(
                first_name=first_name, last_name=last_name, email=email, phone=phone,
                address=address, message=message, extra_data=extra_data, user_id=user_id,
                total_sum=total_sum, total_quantity=total_quantity
            )
            return Response({'message': 'Success'}, status=status.HTTP_201_CREATED)
        except KeyError:
            return Response({'detail': 'Error'}, status=status.HTTP_400_BAD_REQUEST)
