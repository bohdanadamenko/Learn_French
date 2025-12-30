from django.contrib.auth.decorators import login_required
from apps.lessons.selectors import get_lessons_list


@login_required
def index(request):
    # Загружаем все уроки через селектор
    lessons = get_lessons_list()
    return render(request, 'core/index.html', {'lessons': lessons})


def custom_404(request, exception):
    """Custom 404 error page"""
    return render(request, '404.html', status=404)


def custom_500(request):
    """Custom 500 error page"""
    return render(request, '500.html', status=500)
