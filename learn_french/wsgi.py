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

# Auto-initialize SQLite in /tmp on Vercel if external PostgreSQL is not configured
if (os.environ.get('VERCEL') or os.environ.get('AWS_LAMBDA_FUNCTION_NAME')) and not os.environ.get('DATABASE_URL'):
    from pathlib import Path
    from django.core.management import call_command
    init_marker = Path('/tmp') / '.db_initialized'
    if not init_marker.exists():
        try:
            call_command('migrate', interactive=False)
            backup_file = Path(__file__).resolve().parent.parent / 'backup_data.json'
            if backup_file.exists():
                call_command('loaddata', str(backup_file))
            init_marker.touch()
        except Exception as e:
            print(f"Vercel auto-init warning: {e}")

