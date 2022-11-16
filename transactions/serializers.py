from rest_framework import serializers

from category.models import Category
from transactions.models import Transaction
from user.models import User


class UserHider(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)


class TransactionSerializer(serializers.ModelSerializer):
    user = UserHider(read_only=True)

    class Meta:
        model = Transaction
        fields = ('user', 'payment_amount', 'date', 'time', 'category', 'organization', 'description')

