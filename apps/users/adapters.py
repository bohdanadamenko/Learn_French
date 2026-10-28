import os
import logging
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialApp
from decouple import config

logger = logging.getLogger(__name__)


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    """
    Custom adapter for social accounts.
    - Prevents MultipleObjectsReturned if an app is defined in both settings and the database.
    - Prevents SocialApp.DoesNotExist from crashing login/signup template rendering
      when deployed on serverless environments (e.g. Vercel) where SQLite is re-initialized.
    """

    def get_app(self, request, provider, client_id=None):
        apps = self.list_apps(request, provider=provider, client_id=client_id)
        if len(apps) >= 1:
            return apps[0]

        # Fallback: if no app exists in DB or settings, provide an in-memory SocialApp
        # using environment variables so templates never crash with 500 error.
        google_client_id = config('GOOGLE_CLIENT_ID', default=os.environ.get('GOOGLE_CLIENT_ID', ''))
        google_secret = config('GOOGLE_CLIENT_SECRET', default=os.environ.get('GOOGLE_CLIENT_SECRET', ''))

        return SocialApp(
            provider=provider,
            name=provider.capitalize(),
            client_id=google_client_id,
            secret=google_secret,
        )
