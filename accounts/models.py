from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    age = models.PositiveSmallIntegerField(verbose_name='سن', null=True, blank=True)

    class Meta:
        ordering = ['-date_joined']
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر ها'

    def __str__(self):
        return f'{self.username}'
