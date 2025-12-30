from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """
    Custom User model for Learn French project.
    Allows for future extensions like profile pictures, bio, etc.
    """
    email = models.EmailField(_('email address'), unique=True)

    # Add any additional fields here
    # bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.username
