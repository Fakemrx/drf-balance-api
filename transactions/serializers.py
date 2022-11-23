from rest_framework import serializers

from category.models import UserCategories
from transactions.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category = serializers.ChoiceField(choices=list())

    def __init__(self, *args, **kwargs):
        self.user = kwargs['context']['request'].user.id
        super(TransactionSerializer, self).__init__(*args, **kwargs)
        self.fields['user'].default = self.user
        self.fields['category'].choices = tuple(UserCategories.objects.filter(user=self.user).values_list(
            'category_name', flat=True))
        print('in-method value of user:', self.user)

    def create(self, validated_data):
        user = self.context['request'].user
        payment_amount = self.validated_data['payment_amount']
        category = self.validated_data['category']
        organization = self.validated_data['organization']
        description = self.validated_data['description']
        return Transaction.objects.create(user=user, payment_amount=payment_amount, category=category,
                                          organization=organization, description=description)

    class Meta:
        model = Transaction
        fields = ('user', 'payment_amount', 'date', 'time', 'category', 'organization', 'description')
