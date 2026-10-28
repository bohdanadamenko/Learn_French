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

    def pre_social_login(self, request, sociallogin):
        """
        Auto-promote configured admin emails to staff and superuser on Google login.
        """
        super().pre_social_login(request, sociallogin)
        admin_emails = [
            e.strip().lower()
            for e in config('ADMIN_EMAILS', default='adamenko.bogdan@gmail.com').split(',')
            if e.strip()
        ]
        
        email = ''
        if sociallogin.account.extra_data:
            email = sociallogin.account.extra_data.get('email', '')
        if not email and sociallogin.user.email:
            email = sociallogin.user.email

        if email and email.lower() in admin_emails:
            sociallogin.user.is_staff = True
            sociallogin.user.is_superuser = True
            if sociallogin.user.pk:
                sociallogin.user.save(update_fields=['is_staff', 'is_superuser'])

    def save_user(self, request, sociallogin, form=None):
        """
        Ensure newly registered social user gets staff/superuser if email matches admin list.
        """
        user = super().save_user(request, sociallogin, form=form)
        admin_emails = [
            e.strip().lower()
            for e in config('ADMIN_EMAILS', default='adamenko.bogdan@gmail.com').split(',')
            if e.strip()
        ]
        if user.email and user.email.lower() in admin_emails:
            user.is_staff = True
            user.is_superuser = True
            user.save(update_fields=['is_staff', 'is_superuser'])
        return user
