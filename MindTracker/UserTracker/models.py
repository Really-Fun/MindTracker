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


class DailyLog(models.Model):
    MOOD_CHOICES = [(i, str(i)) for i in range(1, 11)]

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="logs",
        verbose_name="ДневнойЛог",
    )
    date = models.DateField(verbose_name="Дата", auto_now_add=True)
    mood = models.PositiveSmallIntegerField(choices=MOOD_CHOICES, default=5)
    took_magnesium = models.BooleanField(verbose_name="Приём Магния")
    notes = models.CharField(verbose_name="Заметки", null=True, blank=True)
