import uuid
import hashlib

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

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"


class DailyLog(models.Model):
    MOOD_CHOICES = [(i, str(i)) for i in range(1, 11)]

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="logs",
        verbose_name="Дневной Лог",
    )
    date = models.DateField(verbose_name="Дата коммита", auto_now_add=True)
    mood = models.PositiveSmallIntegerField(
        choices=MOOD_CHOICES, default=5, verbose_name="Настроение"
    )
    took_magnesium = models.BooleanField(verbose_name="Приём Магния")
    notes = models.CharField(verbose_name="Заметки", null=True, blank=True)
    slug = models.SlugField(
        verbose_name="Хэш коммита", max_length=255, unique=True, editable=False
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            salt = f"{self.user.id}-{uuid.uuid4()}"
            self.slug = hashlib.sha1(salt.encode()).hexdigest()[:12]

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Дневные коммиты"
        verbose_name_plural = "Дневные коммиты"
