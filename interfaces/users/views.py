import requests
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView
from rest_framework import status

from common.views import TitleMixin
from users.forms import UserLoginForm, UserRegistrationForm


class UserLoginView(TitleMixin, FormView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Book Store - Login'
    success_url = reverse_lazy('books:index')
    
    def get(self, request, *args, **kwargs):
        if request.COOKIES.get('Authorization'):
            response = HttpResponseRedirect('http://127.0.0.1:8005')
            response.delete_cookie('Authorization')
            return response
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        req = requests.post('http://127.0.0.1:8000/api/users/login/', data=form.cleaned_data)
        if req.status_code == status.HTTP_200_OK:
            response = super().form_valid(form)
            response.set_cookie('Authorization', req.cookies.get('Authorization'))
            return response
        else:
            form._errors = req.json().get('text')
        return self.form_invalid(form)


class UserRegistrationView(TitleMixin, SuccessMessageMixin, FormView):
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    success_message = 'Registration was successful.\n' \
                      'Check your e-mail for verification this account.'
    title = 'Book Store - Registration'


class EmailVerificationView(TitleMixin, TemplateView):
    template_name = 'users/email_verification.html'
    title = 'Book Store - E-mail confirmation'


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.COOKIES.get('Authorization'):
            response = HttpResponseRedirect('http://127.0.0.1:8001/books/')
            response.delete_cookie('Authorization')
            return response
        else:
            return redirect('http://127.0.0.1:8000/users/login/')
