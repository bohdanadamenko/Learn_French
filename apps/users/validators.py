import re
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class CustomUsernameValidator(RegexValidator):
    regex = r"^[\w!_-]+$"
    message = _("Разрешены только буквы, цифры и знаки !, _, -")
    flags = 0


def validate_username_custom(value):
    """
    Validate that username is at least 4 characters and contains only letters,
    digits, and symbols !, _, -
    """
    if not value or len(value) < 4:
        raise ValidationError(
            _("Имя пользователя должно содержать не менее 4 символов."),
            code="username_too_short",
        )
    if not all(c.isalnum() or c in ("!", "_", "-") for c in value):
        raise ValidationError(
            _("Имя пользователя может содержать только буквы, цифры и знаки !, _, -"),
            code="username_invalid_characters",
        )


class AllowedCharactersPasswordValidator:
    """
    Validate that password is at least 4 characters and contains only letters,
    digits, and symbols !, _, -
    """

    def validate(self, password, user=None):
        if not password or len(password) < 4:
            raise ValidationError(
                _("Пароль должен содержать не менее 4 символов."),
                code="password_too_short",
            )
        if not all(c.isalnum() or c in ("!", "_", "-") for c in password):
            raise ValidationError(
                _("Пароль может содержать только буквы, цифры и знаки !, _, -"),
                code="password_invalid_characters",
            )

    def get_help_text(self):
        return _("Пароль должен содержать не менее 4 символов (разрешены буквы, цифры и знаки !, _, -).")
