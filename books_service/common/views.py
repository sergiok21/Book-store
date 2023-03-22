from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly


class PermissionMixin:
    def get_permissions(self):
        if self.request.user.is_superuser:
            return [AllowAny()]
        return [IsAuthenticatedOrReadOnly()]
