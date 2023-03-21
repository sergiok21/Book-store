import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.views import TitleMixin
from users.forms import UserLoginForm, UserRegistrationForm
from users.models import User


class LoginAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(200)


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Store - Авторизация'

    def get(self, request, *args, **kwargs):
        response = requests.get('http://127.0.0.1:8000/users/api/login/', headers={'Authorization': f'Token {request.COOKIES.get("Authorization", None)}'})
        if response.status_code == 200:
            return redirect('http://127.0.0.1:8001/books/logout/')
        elif request.user.is_authenticated:
            return redirect('http://127.0.0.1:8001/books/')
        else:
            return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            print('')
            HttpResponseRedirect(self.get_success_url())
        else:
            response = super().form_valid(form)

            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            # user = authenticate(self.request, username=username, password=password)
            # login(self.request, user)

            token, created = Token.objects.get_or_create(user=self.request.user)
            response.set_cookie('Authorization', token if token else created)
            return response


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    success_message = 'Регистрация прошла успешно.\nНа Вашу електронную почту отправлено сообщение с подтверждением.'
    title = 'Store - Регистрация'


class EmailVerificationView(TitleMixin, TemplateView):
    template_name = 'users/email_verification.html'
    title = 'Store - Подтверждение электронной почты'


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.COOKIES.get('Authorization'):
            if request.user.is_authenticated:
                print('')
            else:
                print('')
            logout(request)
            return redirect('http://127.0.0.1:8001/books/')
        else:
            return redirect('http://127.0.0.1:8000/users/login/')
