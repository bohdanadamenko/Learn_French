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
    import hashlib
    from pathlib import Path
    from django.core.management import call_command
    
    backup_file = Path(__file__).resolve().parent.parent / 'backup_data.json'
    if backup_file.exists():
        backup_hash = hashlib.md5(backup_file.read_bytes()).hexdigest()[:12]
    else:
        backup_hash = "none"
        
    init_marker = Path('/tmp') / f'.db_init_{backup_hash}'
    if not init_marker.exists():
        try:
            call_command('migrate', interactive=False)
            
            if backup_file.exists():
                try:
                    call_command('loaddata', str(backup_file))
                except Exception as load_err:
                    print(f"Content load notice: {load_err}")

            # Initialize Site and SocialApp for Google OAuth if env vars present
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

            init_marker.touch()
        except Exception as e:
            print(f"Vercel auto-init warning: {e}")

