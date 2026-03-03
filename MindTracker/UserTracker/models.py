from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(
        verbose_name="Аватар пользователя", upload_to="avatars/", null=True, blank=True
    )
    date_birthday = models.DateField(
        verbose_name="Дата рождения",
        blank=True,
        null=True,
    )


class DailyLof(models.Model):
    MOOD_CHOICES = [(i, str(i)) for i in range(1, 11)]
