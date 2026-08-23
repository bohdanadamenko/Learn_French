from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field


class Topic(models.Model):
    """Модель тематического модуля / подгруппы уроков."""
    title = models.CharField(
        max_length=255, verbose_name=_("Название темы"))
    emoji = models.CharField(
        max_length=10, default="📁", verbose_name=_("Эмодзи / Иконка"))
    order = models.IntegerField(
        default=0, verbose_name=_("Порядок сортировки"))

    class Meta:
        verbose_name = _("Тема / Модуль")
        verbose_name_plural = _("Темы / Модули")
        ordering = ['order']
        db_table = 'lessons_topic'

    def __str__(self):
        return f"{self.emoji} {self.title}"


class Lesson(models.Model):
    """Модель для хранения контента урока французского языка."""

    topic = models.ForeignKey(
        Topic,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='lessons',
        verbose_name=_("Тема / Модуль")
    )

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

