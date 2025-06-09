from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_admin_account = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Запрещаем создавать новых пользователей с is_admin_account=True
        if self.is_admin_account and not self.pk:
            raise ValueError("Невозможно создать нового администратора через эту форму")
        super().save(*args, **kwargs)