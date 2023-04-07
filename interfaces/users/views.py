import requests
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, FormView
from rest_framework import status

from common.views import TitleMixin
from .forms import UserLoginForm, UserRegistrationForm


class UserLoginFormView(TitleMixin, FormView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Book Store - Login'
    success_url = reverse_lazy('books:index')

    def form_valid(self, form):
        req = requests.post('http://127.0.0.1:8000/api/users/login/', data=form.cleaned_data)
        if req.status_code == status.HTTP_200_OK:
            response = super().form_valid(form)
            response.set_cookie('Authorization', req.cookies.get('Authorization'))
            response.set_cookie('User', req.cookies.get('User'))
            return response
        else:
            form._errors = req.json().get('text')
        return self.form_invalid(form)


class UserRegistrationFormView(TitleMixin, SuccessMessageMixin, FormView):
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    success_message = 'Registration was successful.\n' \
                      'Check your e-mail for verification this account.'
    title = 'Book Store - Registration'


class EmailVerificationTemplateView(TitleMixin, TemplateView):
    template_name = 'users/email_verification.html'
    title = 'Book Store - E-mail confirmation'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        response = requests.get('http://127.0.0.1:8000/api/users/verification/', params={'code': code})
        if response.status_code == status.HTTP_200_OK:
            return super().get(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('books:index'))
