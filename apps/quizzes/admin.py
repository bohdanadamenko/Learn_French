from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0
    fields = ('text_ru', 'text_uk', 'text_en', 'text_fr', 'is_correct')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text_ru', 'text_uk', 'text_en', 'text_fr', 'lesson_ru', 'lesson_uk', 'lesson_en', 'lesson_fr', 'order')
    list_display_links = ('text_ru', 'text_uk', 'text_en', 'text_fr')
    list_filter = ('lesson',)
    inlines = [ChoiceInline]
    
    def lesson_ru(self, obj): return obj.lesson.title_ru
    def lesson_uk(self, obj): return obj.lesson.title_uk
    def lesson_en(self, obj): return obj.lesson.title_en
    def lesson_fr(self, obj): return obj.lesson.title_fr
    
    lesson_ru.short_description = _("Урок (RU)")
    lesson_uk.short_description = _("Урок (UK)")
    lesson_en.short_description = _("Урок (EN)")
    lesson_fr.short_description = _("Урок (FR)")

    def changelist_view(self, request, extra_context=None):
        """Инъекция JSON с переводами уроков для JS через заголовок страницы"""
        from django.utils.safestring import mark_safe
        from apps.quizzes.selectors import get_lesson_translations_json
        
        json_data = get_lesson_translations_json()
        script = f'<script id="lesson-translations-data" type="application/json">{json_data}</script>'
        
        extra_context = extra_context or {}
        # Добавляем скрипт к заголовку (он не будет виден визуально, но будет в DOM)
        title = "Выберите вопрос для изменения"
        extra_context['title'] = mark_safe(title + script)
        
        return super().changelist_view(request, extra_context=extra_context)

    fieldsets = (
        (_('Связь'), {'fields': ('lesson', 'order')}),
        (_('Русский язык (RU)'), {'fields': ('text_ru',)}),
        (_('Українська мова (UK)'), {'fields': ('text_uk',)}),
        (_('English (EN)'), {'fields': ('text_en',)}),
        (_('Français (FR)'), {'fields': ('text_fr',)}),
    )

    class Media:
        js = ('core/js/admin_lang_tabs.js',)
