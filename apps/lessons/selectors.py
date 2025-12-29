from django.db.models import QuerySet
from .models import Lesson

def get_lessons_list() -> QuerySet[Lesson]:
    """
    Returns all lessons ordered by their display order.
    """
    return Lesson.objects.all().order_by('order')
