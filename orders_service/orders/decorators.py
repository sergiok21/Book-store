import requests
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed


def token_required(view_func):
    def wrapper(request, *args, **kwargs):
        token = args[0].META.get('HTTP_AUTHORIZATION')
        if not token:
            raise AuthenticationFailed('Authentication credentials were not provided')
        response = requests.get('http://127.0.0.1:8000/api/users/login/', headers={'Authorization': token})
        if response.status_code != status.HTTP_200_OK:
            raise AuthenticationFailed('Invalid token')
        return view_func(request, *args, **kwargs)
    return wrapper


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    return wrapper
