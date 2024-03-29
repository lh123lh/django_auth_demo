from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)

    class Meta(AbstractUser.Meta):
        pass