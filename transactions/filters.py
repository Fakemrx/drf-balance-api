from django_filters import rest_framework as filters

from transactions.models import Transaction


class TransactionFilter(filters.FilterSet):
    date = filters.DateFromToRangeFilter()
    time = filters.TimeRangeFilter()
    payment_amount = filters.RangeFilter()

    class Meta:
        model = Transaction
        fields = ['time', 'payment_amount', 'date']
