from django.urls import path

from users.views import LoginAPIView, RegistrationAPIView, CallbackView, UserAPIView, LogoutAPIView, VerificationAPIView

app_name = 'users'


urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('registration/', RegistrationAPIView.as_view(), name='registration'),
    path('callback/', CallbackView.as_view(), name='callback'),
    path('user/<int:id>/', UserAPIView.as_view(), name='user'),
    path('verification/', VerificationAPIView.as_view(), name='verification'),
]
