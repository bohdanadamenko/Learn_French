"""
WSGI config for learn_french project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn_french.settings')

application = get_wsgi_application()

# Vercel WSGI entrypoint alias
app = application

# Auto-initialize database on Vercel boot (both for SQLite and Neon PostgreSQL)
if os.environ.get('VERCEL') or os.environ.get('AWS_LAMBDA_FUNCTION_NAME'):
    from pathlib import Path
    from django.core.management import call_command

    # 1. Run migrations if not yet run on this container
    migrate_marker = Path('/tmp') / '.db_migrated'
    if not migrate_marker.exists():
        try:
            call_command('migrate', interactive=False)
            migrate_marker.touch()
        except Exception as e:
            print(f"Vercel migrate notice: {e}")

    # 2. Seed lessons if Lesson table is empty (or forced)
    try:
        from apps.lessons.models import Lesson
        force_reload = os.environ.get('FORCE_RELOAD_FIXTURES', '').lower() in ('1', 'true', 'yes')
        if force_reload or not Lesson.objects.exists():
            try:
                call_command('loaddata', 'initial_lessons')
            except Exception:
                backup_file = Path(__file__).resolve().parent.parent / 'backup_data.json'
                if backup_file.exists():
                    call_command('loaddata', str(backup_file))
            print(f"Initialized lessons, count: {Lesson.objects.count()}")
    except Exception as load_err:
        print(f"Content load notice: {load_err}")

    # 3. Ensure admin permissions for owner
    try:
        from apps.users.models import User
        from django.db.models import Q
        User.objects.filter(
            Q(email__iexact='adamenko.bogdan@gmail.com') | Q(username__iexact='Bohdan')
        ).update(is_staff=True, is_superuser=True)
    except Exception as admin_err:
        print(f"Admin init warning: {admin_err}")

    # 4. Initialize Site and SocialApp for Google OAuth if env vars present
    google_client_id = os.environ.get('GOOGLE_CLIENT_ID')
    google_secret = os.environ.get('GOOGLE_CLIENT_SECRET')
    if google_client_id and google_secret:
        try:
            from django.contrib.sites.models import Site
            from allauth.socialaccount.models import SocialApp
            site, _ = Site.objects.get_or_create(id=1, defaults={'domain': 'www.learn-french.be', 'name': 'FrenchLessons'})
            if site.domain == 'example.com':
                site.domain = 'www.learn-french.be'
                site.name = 'FrenchLessons'
                site.save()
            app, _ = SocialApp.objects.get_or_create(
                provider='google',
                defaults={
                    'name': 'FrenchLessons',
                    'client_id': google_client_id,
                    'secret': google_secret,
                }
            )
            app.client_id = google_client_id
            app.secret = google_secret
            app.sites.add(site)
            app.save()
        except Exception as app_err:
            print(f"Vercel SocialApp init warning: {app_err}")

