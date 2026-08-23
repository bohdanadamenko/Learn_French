from django.db.models import QuerySet, Prefetch
from .models import Lesson, Topic


def get_lessons_list() -> QuerySet[Lesson]:
    """
    Returns all lessons ordered by their display order.
    """
    return Lesson.objects.all().select_related('topic').order_by('order')


def get_topics_with_lessons() -> QuerySet[Topic]:
    """
    Returns all topics with preloaded ordered lessons.
    """
    return Topic.objects.all().prefetch_related(
        Prefetch('lessons', queryset=Lesson.objects.all().order_by('order'))
    ).order_by('order')

