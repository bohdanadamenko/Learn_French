from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .validators import validate_username_custom, CustomUsernameValidator


class User(AbstractUser):
    """
    Custom User model for FrenchLessons project.
    Allows for future extensions like profile pictures, bio, etc.
    """
    username_validator = CustomUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Не менее 4 символов (буквы, цифры и знаки !, _, -).'),
        validators=[username_validator, validate_username_custom],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), unique=True)

    def __str__(self):
        return self.username
