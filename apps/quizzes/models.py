from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.lessons.models import Lesson

class Question(models.Model):
    """Модель вопроса для теста после урока."""
    lesson = models.ForeignKey(Lesson, related_name='questions', on_delete=models.CASCADE, verbose_name=_("Урок"))
    
    text = models.TextField(verbose_name=_("Текст вопроса"), blank=True, null=True)
    
    order = models.IntegerField(default=0, verbose_name=_("Порядок"))

    class Meta:
        verbose_name = _("Вопрос")
        verbose_name_plural = _("Вопросы")
        ordering = ['order']
        db_table = 'lessons_question' # Preserve old table name

    def __str__(self):
        return f"{self.lesson} - {self.text[:50] if self.text else ''}"


class Choice(models.Model):
    """Модель варианта ответа."""
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    
    text = models.CharField(max_length=255, verbose_name=_("Текст ответа"), blank=True, null=True)
    
    is_correct = models.BooleanField(default=False, verbose_name=_("Это правильный ответ?"))

    class Meta:
        verbose_name = _("Вариант ответа")
        verbose_name_plural = _("Варианты ответов")
        db_table = 'lessons_choice' # Preserve old table name

    def __str__(self):
        return self.text or ""
