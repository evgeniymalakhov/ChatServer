from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
import uuid


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'users/{str(uuid.uuid4())}'


class User(AbstractUser):
    username = None
    email = models.EmailField(_('Email address'), unique=True)
    # photo = models.ImageField(upload_to=user_directory_path)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
