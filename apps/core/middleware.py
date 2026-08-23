from django.conf import settings
from django.utils import translation


class DefaultLanguageMiddleware:
    """
    Ensures 'uk' is the default language when the user has not explicitly chosen a language.
    Prevents browser Accept-Language header from defaulting to Russian or other languages.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language_cookie = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME, None)
        session_language = request.session.get('django_language', None) if hasattr(request, 'session') else None

        if not language_cookie and not session_language:
            translation.activate('uk')
            request.LANGUAGE_CODE = 'uk'

        response = self.get_response(request)
        return response
