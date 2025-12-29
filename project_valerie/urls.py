# project_valerie/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('lessons.urls')),  # <--- Отправляем / в lessons
]

# Custom error handlers
handler404 = 'lessons.views.custom_404'
handler500 = 'lessons.views.custom_500'
