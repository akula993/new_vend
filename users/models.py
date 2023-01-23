from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
#https://django.fun/ru/articles/tutorials/django-custom-user-model/