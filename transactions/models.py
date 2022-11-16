from django.db import models

from category.models import Category
from user.models import User


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.deletion.CASCADE, verbose_name='Транзакция от')
    payment_amount = models.DecimalField(default=0, decimal_places=2, max_digits=20, verbose_name='Сумма платежа')
    date = models.DateField(auto_now=True, verbose_name='Дата транзакции')
    time = models.TimeField(auto_now=True, verbose_name='Время транзакции')
    category = models.ForeignKey(Category, on_delete=models.deletion.SET_NULL, verbose_name='Категория', null=True)
    organization = models.TextField(max_length=60, verbose_name='Организация')
    description = models.TextField(max_length=300, null=True, blank=True, verbose_name='Описание/комментарий')

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

    def __str__(self):
        return f'"{self.user.fio}" -> "{self.organization}" ({self.category.category.name}) | {self.payment_amount} р.'
