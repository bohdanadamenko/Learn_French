import re
from django.core.management.base import BaseCommand
from lessons.models import Lesson

class Command(BaseCommand):
    help = 'Removes numbering (e.g., "1. ") from lesson titles.'

    def handle(self, *args, **options):
        lessons = Lesson.objects.all()
        count = 0
        for lesson in lessons:
            # Regex to match numbering:
            # 1. At start of string: ^\d+\.\s*
            # 2. Preceded by space (e.g. after emoji): (?<=\s)\d+\.\s*
            # We'll use a pattern that captures the prefix (start or space) and keeps it.
            new_title = re.sub(r'(^|\s)\d+\.\s+', r'\1', lesson.title)
            
            if new_title != lesson.title:
                self.stdout.write(f'Renaming: "{lesson.title}" -> "{new_title}"')
                lesson.title = new_title
                lesson.save()
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully updated {count} lesson titles.'))
