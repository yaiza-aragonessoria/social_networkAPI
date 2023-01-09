from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings



class User(AbstractUser):
    # Field used for authentication
    USERNAME_FIELD = 'email'

    # Additional fields required when using createsuperuser (USERNAME_FIELD and passwords are always required)
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(unique=True)

    following = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='followed_by', blank=True, symmetrical=False)

    def __str__(self):
        return self.username