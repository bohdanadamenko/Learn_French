from modeltranslation.translator import register, TranslationOptions
from .models import Lesson

@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title', 'content_html')
