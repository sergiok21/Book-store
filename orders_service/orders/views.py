import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .authentication import CustomTokenAuthentication, CustomIsAuthenticated
from .models import Order
from .serializers import OrderSerializer


class OrderModelViewSet(ModelViewSet):
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
            order = Order.objects.create(
                first_name=first_name, last_name=last_name, email=email, phone=phone,
                address=address, message=message, extra_data=extra_data, user_id=user_id,
                total_sum=total_sum, total_quantity=total_quantity
            )

            headers = {'Authorization': f'{request.META.get("HTTP_AUTHORIZATION")}'}
            cookies = {'User': request.COOKIES.get('User')}

            requests.post('http://127.0.0.1:8000/api/users/echo-all/',
                          data={
                              'order': order.order_number,
                              'first_name': first_name,
                              'last_name': last_name,
                              'phone': phone,
                              'message': message,
                              'total_sum': total_sum,
                              'total_quantity': total_quantity,
                              'extra_data': extra_data
                          },
                          headers=headers,
                          cookies=cookies)
            return Response({'message': 'Success'}, status=status.HTTP_201_CREATED)
        except KeyError:
            return Response({'detail': 'Error'}, status=status.HTTP_400_BAD_REQUEST)
