from lessons.models import Lesson
import json

lessons_data = []
for l in Lesson.objects.all().order_by('order'):
    lessons_data.append({
        'id': l.data_lesson_id,
        'title_ru': l.title_ru,
        'content_ru': l.content_html_ru
    })

with open('lessons_export.json', 'w', encoding='utf-8') as f:
    json.dump(lessons_data, f, ensure_ascii=False, indent=4)

print(f"Exported {len(lessons_data)} lessons to lessons_export.json")
