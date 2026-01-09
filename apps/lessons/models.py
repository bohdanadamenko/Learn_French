from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

class Lesson(models.Model):
    """Модель для хранения контента урока французского языка."""

    # Поля для разных языков удалены в пользу django-modeltranslation
    
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
        return self.title
