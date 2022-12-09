from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from category.models import UserCategories


class User(AbstractUser):
    fio = models.TextField(max_length=100, null=False, blank=False, verbose_name='ФИО')
    account_balance = models.DecimalField(default=0, decimal_places=2, max_digits=20, verbose_name='Баланс счёта')

    REQUIRED_FIELDS = ['fio', 'email']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.fio} aka {self.username}'


@receiver(post_save, sender=User)
def update_stock(sender, instance, **kwargs):
    user = instance
    default_categories_list = ("Забота о себе", "Зарплата", "Здоровье и фитнес", "Кафе и рестораны", "Машина",
                               "Образование", "Отдых и развлечения", "Платежи, комиссии",
                               "Покупки: одежда, техника", "Продукты", "Проезд")
    for category in default_categories_list:
        category_to_add = UserCategories(category_name=category, user=user)
        category_to_add.save()
