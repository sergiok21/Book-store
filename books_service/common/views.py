from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly


class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context


class PermissionMixin:
    def get_permissions(self):
        if self.request.user.is_superuser:
            return [AllowAny()]
        return [IsAuthenticatedOrReadOnly()]
