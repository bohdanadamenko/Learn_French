# lessons/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Этот маршрут правильный. Он вызывает views.index.
    path('', views.index, name='index'),
]
