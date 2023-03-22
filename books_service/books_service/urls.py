from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('api/books/admin/', admin.site.urls),
    path('', lambda req: redirect('api/books/')),
    path('api/books/', include('books.urls', namespace='books')),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')),)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
