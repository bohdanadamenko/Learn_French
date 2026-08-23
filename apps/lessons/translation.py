from modeltranslation.translator import register, TranslationOptions
from .models import Lesson, Topic


@register(Topic)
class TopicTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title', 'content_html')

