from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/users/admin/', admin.site.urls),
    path('api/users/', include('users.urls', namespace='users')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')),)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
