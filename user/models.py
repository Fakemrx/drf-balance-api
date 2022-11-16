from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    fio = models.TextField(max_length=100, null=False, blank=False, verbose_name='ФИО')

    REQUIRED_FIELDS = ['fio']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.fio} aka {self.username}'
