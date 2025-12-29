# project_valerie/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('', include('lessons.urls')),  # <--- Отправляем / в lessons
]

# Media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom error handlers
handler404 = 'lessons.views.custom_404'
handler500 = 'lessons.views.custom_500'
