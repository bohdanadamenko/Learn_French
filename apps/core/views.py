from django.shortcuts import render
from apps.lessons.models import Lesson
from apps.lessons.selectors import get_lessons_list, get_topics_with_lessons


def index(request):
    if request.GET.get('seed_now') == '1':
        import traceback
        from django.core.management import call_command
        from django.http import HttpResponse
        output = []
        try:
            call_command('loaddata', 'initial_lessons')
            output.append(f"SUCCESS loading initial_lessons! Lessons: {Lesson.objects.count()}")
        except Exception as e:
            output.append(f"initial_lessons failed: {e}\n{traceback.format_exc()}")
            try:
                from pathlib import Path
                backup_file = Path(__file__).resolve().parent.parent.parent / 'backup_data.json'
                call_command('loaddata', str(backup_file))
                output.append("SUCCESS with backup_data.json!")
            except Exception as e2:
                output.append(f"backup_data.json failed: {e2}\n{traceback.format_exc()}")
        return HttpResponse("\n".join(output), content_type="text/plain")

    lessons = get_lessons_list()
    topics = get_topics_with_lessons()
    return render(request, 'core/index.html', {
        'lessons': lessons,
        'topics': topics,
    })



def custom_404(request, exception):
    """Custom 404 error page"""
    return render(request, '404.html', status=404)


def custom_500(request):
    """Custom 500 error page"""
    return render(request, '500.html', status=500)
