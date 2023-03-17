from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('users/admin/', admin.site.urls),
    path('', lambda req: redirect('books/')),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')),)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
