import json
from django.db.models import QuerySet
from apps.lessons.models import Lesson

def get_lesson_translations_json(lessons: QuerySet[Lesson] = None) -> str:
    """
    Generates a JSON string containing translation data for all lessons.
    Used for injecting data into the admin interface via JavaScript.
    """
    if lessons is None:
        lessons = Lesson.objects.all()
        
    data = {
        str(l.id): {
            'ru': l.title_ru, 
            'uk': l.title_uk, 
            'en': l.title_en, 
            'fr': l.title_fr
        } 
        for l in lessons
    }
    return json.dumps(data)
