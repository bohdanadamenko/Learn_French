from django.core.management.base import BaseCommand
from lessons.models import Lesson

class Command(BaseCommand):
    help = 'Migrates existing lesson content to the new RU fields'

    def handle(self, *args, **options):
        lessons = Lesson.objects.all()
        count = 0
        for lesson in lessons:
            if not lesson.title_ru:
                lesson.title_ru = lesson.title
            if not lesson.content_html_ru:
                lesson.content_html_ru = lesson.content_html
            lesson.save()
            count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully migrated {count} lessons to RU fields'))
