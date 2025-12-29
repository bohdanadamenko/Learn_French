from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Lesson

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'title_uk', 'title_en', 'title_fr', 'data_lesson_id', 'order', 'date_added')
    list_display_links = ('title_ru', 'title_uk', 'title_en', 'title_fr')
    search_fields = ('title_ru', 'title_en', 'content_html_ru', 'content_html_en')
    list_editable = ('order',)

    fieldsets = (
        (_('Основные настройки'), {
            'fields': ('data_lesson_id', 'order')
        }),
        (_('Русский язык (RU)'), {
            'fields': ('title_ru', 'content_html_ru'),
        }),
        (_('Українська мова (UK)'), {
            'fields': ('title_uk', 'content_html_uk'),
        }),
        (_('English (EN)'), {
            'fields': ('title_en', 'content_html_en'),
        }),
        (_('Français (FR)'), {
            'fields': ('title_fr', 'content_html_fr'),
        }),
    )
    
    class Media:
        js = ('core/js/admin_lang_tabs.js',)
