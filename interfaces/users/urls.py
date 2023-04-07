from django.shortcuts import redirect
from django.urls import path

from .views import UserLoginFormView, UserRegistrationFormView, EmailVerificationTemplateView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginFormView.as_view(), name='login'),
    path('logout/', lambda req: redirect('http://127.0.0.1:8000/api/users/logout/'), name='logout'),
    path('registration/', UserRegistrationFormView.as_view(), name='registration'),
    path('verification/<str:email>/<uuid:code>/', EmailVerificationTemplateView.as_view(), name='email_verification'),

    path('accounts/google/', lambda req: redirect('http://127.0.0.1:8000/accounts/google/login/'), name='google'),
    path('accounts/github/', lambda req: redirect('http://127.0.0.1:8000/accounts/github/login/'), name='github'),
]
