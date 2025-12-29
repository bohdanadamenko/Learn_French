from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.lessons.models import Lesson

class Question(models.Model):
    """Модель вопроса для теста после урока."""
    lesson = models.ForeignKey(Lesson, related_name='questions', on_delete=models.CASCADE, verbose_name=_("Урок"))
    
    text_ru = models.TextField(verbose_name=_("Текст вопроса (RU)"), blank=True, null=True)
    text_uk = models.TextField(verbose_name=_("Текст вопроса (UK)"), blank=True, null=True)
    text_en = models.TextField(verbose_name=_("Текст вопроса (EN)"), blank=True, null=True)
    text_fr = models.TextField(verbose_name=_("Текст вопроса (FR)"), blank=True, null=True)
    
    order = models.IntegerField(default=0, verbose_name=_("Порядок"))

    class Meta:
        verbose_name = _("Вопрос")
        verbose_name_plural = _("Вопросы")
        ordering = ['order']
        db_table = 'lessons_question' # Preserve old table name

    def __str__(self):
        from django.utils.translation import get_language
        lang = get_language()
        text = self.text_ru
        if lang == 'uk': text = self.text_uk or self.text_ru
        elif lang == 'en': text = self.text_en or self.text_ru
        elif lang == 'fr': text = self.text_fr or self.text_ru
        return f"{self.lesson} - {text[:50] if text else ''}"


class Choice(models.Model):
    """Модель варианта ответа."""
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    
    text_ru = models.CharField(max_length=255, verbose_name=_("Текст ответа (RU)"), blank=True, null=True)
    text_uk = models.CharField(max_length=255, verbose_name=_("Текст ответа (UK)"), blank=True, null=True)
    text_en = models.CharField(max_length=255, verbose_name=_("Текст ответа (EN)"), blank=True, null=True)
    text_fr = models.CharField(max_length=255, verbose_name=_("Текст ответа (FR)"), blank=True, null=True)
    
    is_correct = models.BooleanField(default=False, verbose_name=_("Это правильный ответ?"))

    class Meta:
        verbose_name = _("Вариант ответа")
        verbose_name_plural = _("Варианты ответов")
        db_table = 'lessons_choice' # Preserve old table name

    def __str__(self):
        from django.utils.translation import get_language
        lang = get_language()
        if lang == 'uk': return self.text_uk or self.text_ru
        elif lang == 'en': return self.text_en or self.text_ru
        elif lang == 'fr': return self.text_fr or self.text_ru
        return self.text_ru or ""
