from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

class Lesson(models.Model):
    """Модель для хранения контента урока французского языка."""

    # Поля для разных языков
    title_ru = models.CharField(max_length=255, verbose_name=_("Заголовок (RU)"), blank=True, null=True)
    title_uk = models.CharField(max_length=255, verbose_name=_("Заголовок (UK)"), blank=True, null=True)
    title_en = models.CharField(max_length=255, verbose_name=_("Заголовок (EN)"), blank=True, null=True)
    title_fr = models.CharField(max_length=255, verbose_name=_("Заголовок (FR)"), blank=True, null=True)

    content_html_ru = CKEditor5Field(verbose_name=_("Контент (RU)"), blank=True, null=True, config_name='extends')
    content_html_uk = CKEditor5Field(verbose_name=_("Контент (UK)"), blank=True, null=True, config_name='extends')
    content_html_en = CKEditor5Field(verbose_name=_("Контент (EN)"), blank=True, null=True, config_name='extends')
    content_html_fr = CKEditor5Field(verbose_name=_("Контент (FR)"), blank=True, null=True, config_name='extends')

    # Старые поля (оставляем для миграции)
    title = models.CharField(
        max_length=255, verbose_name=_("Заголовок и эмодзи (напр., Урок 1: 🇫🇷 Фонетика)"))
    
    data_lesson_id = models.CharField(
        max_length=20, unique=True, verbose_name=_("ID урока (lesson1, lesson2...)"))
    
    content_html = CKEditor5Field(
        verbose_name=_("HTML-содержимое урока (с тегами H3, P, UL и т.д.)"), config_name='extends')

    # Порядок сортировки в меню
    order = models.IntegerField(default=0, verbose_name=_("Порядок сортировки"))

    date_added = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания"))

    class Meta:
        verbose_name = _("Урок")
        verbose_name_plural = _("Уроки")
        ordering = ['order']
        db_table = 'lessons_lesson'  # Preserve old table name

    def __str__(self):
        from django.utils.translation import get_language
        lang = get_language()
        if lang == 'uk':
            return self.title_uk or self.title_ru
        elif lang == 'en':
            return self.title_en or self.title_ru
        elif lang == 'fr':
            return self.title_fr or self.title_ru
        return self.title_ru or self.title
