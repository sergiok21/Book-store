from django.http import HttpResponseRedirect
from django.views import View
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import RegistrationSerializer, TokenSerializer, UserSerializer


class LoginAPIView(APIView):
    serializer_class = TokenSerializer
    permission_classes = []

    @authentication_classes([TokenAuthentication])
    def get(self, request):
        if request.query_params.get('token'):
            token = request.query_params.get('token')
            token_obj = Token.objects.filter(key=token)
            if token_obj.exists():
                token = token_obj.first()
                serializer = TokenSerializer(token)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        if user is None:
            return Response({'error': 'Invalid username'}, status=status.HTTP_400_BAD_REQUEST)
        elif not user.check_password(password):
            return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            token, created = Token.objects.get_or_create(user=user)

            response_data = {'token': token.key if token else created}
            response = Response(response_data, status=status.HTTP_200_OK)
            response.set_cookie('Authorization', token.key if token else created)
            return response


class RegistrationAPIView(APIView):
    serializer_class = RegistrationSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.id)


class LogoutAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        if request.COOKIES.get('Authorization'):
            response = HttpResponseRedirect('http://127.0.0.1:8005/books/')
            response.delete_cookie('Authorization')
            return response
        else:
            return Response({'detail': 'Logout without token'}, status=status.HTTP_401_UNAUTHORIZED)


class CallbackView(View):
    def get(self, request):
        response = HttpResponseRedirect('http://127.0.0.1:8005')
        token, created = Token.objects.get_or_create(user=self.request.user)
        response['HTTP_AUTHORIZATION'] = f'Token ' + token.key if token else created
        response.set_cookie('Authorization', token.key if token else created)
        return response
