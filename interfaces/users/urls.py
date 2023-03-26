from django.shortcuts import redirect
from django.urls import path

from .views import UserLoginView, UserRegistrationView, EmailVerificationView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),
    # path('logout/', LogoutView.as_view(), name='logout'),

    path('accounts/google/', lambda req: redirect('http://127.0.0.1:8000/accounts/google/login/'), name='google'),
    path('accounts/github/', lambda req: redirect('http://127.0.0.1:8000/accounts/github/login/'), name='github'),
]
