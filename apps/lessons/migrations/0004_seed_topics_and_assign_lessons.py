from django.db import migrations


def seed_topics_and_assign_lessons(apps, schema_editor):
    Topic = apps.get_model('lessons_app', 'Topic')
    Lesson = apps.get_model('lessons_app', 'Lesson')

    topics_data = [
        {
            'order': 1,
            'emoji': '🚀',
            'title': 'Основи та перші кроки',
            'title_uk': 'Основи та перші кроки',
            'title_ru': 'Основы и первые шаги',
            'title_en': 'Basics & First Steps',
            'title_fr': 'Les bases et premiers pas',
            'lessons': ['lesson1', 'lesson-be', 'lesson2', 'lesson-numbers', 'lesson-calendar']
        },
        {
            'order': 2,
            'emoji': '🧱',
            'title': 'Базова граматика',
            'title_uk': 'Базова граматика',
            'title_ru': 'Базовая грамматика',
            'title_en': 'Basic Grammar',
            'title_fr': 'Grammaire de base',
            'lessons': ['lesson3', 'lesson4', 'lesson-avoir', 'lesson-negation', 'lesson-partitive']
        },
        {
            'order': 3,
            'emoji': '⚡',
            'title': 'Дієслова, часи та запитання',
            'title_uk': 'Дієслова, часи та запитання',
            'title_ru': 'Глаголы, времена и вопросы',
            'title_en': 'Verbs, Tenses & Questions',
            'title_fr': 'Verbes, temps et questions',
            'lessons': ['lesson-er-verbs', 'lesson-questions', 'lesson-futur-proche', 'lesson-passe-compose', 'lesson-reflexive']
        },
        {
            'order': 4,
            'emoji': '🌍',
            'title': 'Лексика та теми',
            'title_uk': 'Лексика та теми',
            'title_ru': 'Лексика и темы',
            'title_en': 'Vocabulary & Topics',
            'title_fr': 'Vocabulaire et thèmes',
            'lessons': ['lesson-adjectives', 'lesson-prepositions', 'lesson-family', 'lesson-colors', 'lesson-transport', 'lesson-movies', 'lesson-video']
        }
    ]

    for t_data in topics_data:
        lesson_ids = t_data.pop('lessons')
        topic, _ = Topic.objects.get_or_create(
            order=t_data['order'],
            defaults=t_data
        )
        Lesson.objects.filter(data_lesson_id__in=lesson_ids).update(topic=topic)


def reverse_seed_topics(apps, schema_editor):
    Topic = apps.get_model('lessons_app', 'Topic')
    Lesson = apps.get_model('lessons_app', 'Lesson')
    Lesson.objects.all().update(topic=None)
    Topic.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('lessons_app', '0003_topic_lesson_topic'),
    ]

    operations = [
        migrations.RunPython(seed_topics_and_assign_lessons, reverse_seed_topics),
    ]
