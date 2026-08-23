from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Lesson, Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('emoji', 'title_ru', 'title_uk', 'title_en', 'title_fr', 'order')
    list_display_links = ('title_ru', 'title_uk', 'title_en', 'title_fr')
    list_editable = ('order',)
    search_fields = ('title_ru', 'title_uk', 'title_en', 'title_fr')

    fieldsets = (
        (_('Основные настройки'), {
            'fields': ('emoji', 'order')
        }),
        (_('Русский язык (RU)'), {
            'fields': ('title_ru',),
        }),
        (_('Українська мова (UK)'), {
            'fields': ('title_uk',),
        }),
        (_('English (EN)'), {
            'fields': ('title_en',),
        }),
        (_('Français (FR)'), {
            'fields': ('title_fr',),
        }),
    )

    class Media:
        js = ('core/js/admin_lang_tabs.js',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'topic', 'data_lesson_id', 'order', 'date_added')
    list_display_links = ('title_ru',)
    list_filter = ('topic',)
    search_fields = ('title_ru', 'title_en', 'content_html_ru', 'content_html_en')
    list_editable = ('order', 'topic')

    fieldsets = (
        (_('Основные настройки'), {
            'fields': ('topic', 'data_lesson_id', 'order')
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

