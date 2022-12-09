from django.db import models


class UserCategories(models.Model):
    category_name = models.TextField(unique=False, max_length=60, verbose_name='Название категории')
    user = models.ForeignKey('user.User', on_delete=models.deletion.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Категория пользователя'
        verbose_name_plural = 'Категории пользователя'

    def __str__(self):
        return f'{self.category_name}'
