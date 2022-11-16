from django.db import models

from user.models import User


class CategoryList(models.Model):
    name = models.TextField(unique=True, max_length=60, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.deletion.CASCADE, verbose_name='Пользователь')
    category = models.ForeignKey(CategoryList, on_delete=models.deletion.SET_NULL, verbose_name='Категория', null=True)

    class Meta:
        verbose_name = 'Категория пользователя'
        verbose_name_plural = 'Категории пользователя'

    def __str__(self):
        return f'{self.category.name}'
