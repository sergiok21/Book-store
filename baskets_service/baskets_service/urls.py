from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('api/baskets/admin/', admin.site.urls),
    path('', lambda req: redirect('api/baskets/')),
    path('api/baskets/', include('baskets.urls', namespace='baskets')),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')),)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
