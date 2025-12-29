# lessons/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field


class Lesson(models.Model):
    """Модель для хранения контента урока французского языка."""

    # Поля для разных языков
    title_ru = models.CharField(max_length=255, verbose_name=_("Заголовок (RU)"), blank=True, null=True)
    title_ua = models.CharField(max_length=255, verbose_name=_("Заголовок (UA)"), blank=True, null=True)
    title_en = models.CharField(max_length=255, verbose_name=_("Заголовок (EN)"), blank=True, null=True)
    title_fr = models.CharField(max_length=255, verbose_name=_("Заголовок (FR)"), blank=True, null=True)

    content_html_ru = CKEditor5Field(verbose_name=_("Контент (RU)"), blank=True, null=True, config_name='extends')
    content_html_ua = CKEditor5Field(verbose_name=_("Контент (UA)"), blank=True, null=True, config_name='extends')
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
        # Сортировка по полю 'order'
        ordering = ['order']

    def __str__(self):
        from django.utils.translation import get_language
        lang = get_language()
        if lang == 'uk':
            return self.title_ua or self.title_ru
        elif lang == 'en':
            return self.title_en or self.title_ru
        elif lang == 'fr':
            return self.title_fr or self.title_ru
        return self.title_ru or self.title


class Question(models.Model):
    """Модель вопроса для теста после урока."""
    lesson = models.ForeignKey(Lesson, related_name='questions', on_delete=models.CASCADE, verbose_name=_("Урок"))
    
    text_ru = models.TextField(verbose_name=_("Текст вопроса (RU)"), blank=True, null=True)
    text_ua = models.TextField(verbose_name=_("Текст вопроса (UA)"), blank=True, null=True)
    text_en = models.TextField(verbose_name=_("Текст вопроса (EN)"), blank=True, null=True)
    text_fr = models.TextField(verbose_name=_("Текст вопроса (FR)"), blank=True, null=True)
    
    order = models.IntegerField(default=0, verbose_name=_("Порядок"))

    class Meta:
        verbose_name = _("Вопрос")
        verbose_name_plural = _("Вопросы")
        ordering = ['order']

    def __str__(self):
        from django.utils.translation import get_language
        lang = get_language()
        text = self.text_ru
        if lang == 'uk': text = self.text_ua or self.text_ru
        elif lang == 'en': text = self.text_en or self.text_ru
        elif lang == 'fr': text = self.text_fr or self.text_ru
        return f"{self.lesson} - {text[:50] if text else ''}"


class Choice(models.Model):
    """Модель варианта ответа."""
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    
    text_ru = models.CharField(max_length=255, verbose_name=_("Текст ответа (RU)"), blank=True, null=True)
    text_ua = models.CharField(max_length=255, verbose_name=_("Текст ответа (UA)"), blank=True, null=True)
    text_en = models.CharField(max_length=255, verbose_name=_("Текст ответа (EN)"), blank=True, null=True)
    text_fr = models.CharField(max_length=255, verbose_name=_("Текст ответа (FR)"), blank=True, null=True)
    
    is_correct = models.BooleanField(default=False, verbose_name=_("Это правильный ответ?"))

    class Meta:
        verbose_name = _("Вариант ответа")
        verbose_name_plural = _("Варианты ответов")

    def __str__(self):
        from django.utils.translation import get_language
        lang = get_language()
        if lang == 'uk': return self.text_ua or self.text_ru
        elif lang == 'en': return self.text_en or self.text_ru
        elif lang == 'fr': return self.text_fr or self.text_ru
        return self.text_ru or ""
