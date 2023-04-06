from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import BasePermission, AllowAny

from .decorators import token_required


class CustomTokenAuthentication(TokenAuthentication):
    @token_required
    def authenticate(self, request):
        return None, None


class CustomIsAuthenticated(CustomTokenAuthentication, BasePermission):
    @token_required
    def has_permission(self, request, view):
        return [AllowAny]
