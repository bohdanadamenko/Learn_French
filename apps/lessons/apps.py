from django.apps import AppConfig

class LessonsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.lessons'
    label = 'lessons_app'  # Avoid conflict with legacy 'lessons'
