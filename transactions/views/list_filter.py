from decimal import Decimal

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from transactions.filters import TransactionFilter
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class TransactionsAPIView(generics.ListAPIView):
    def get_queryset(self):
        if self.request.user.is_authenticated:
            sort = self.request.GET.get("sort")
            if sort:
                return Transaction.objects.filter(user=self.request.user.id).order_by(sort)
            return Transaction.objects.filter(user=self.request.user.id)
        else:
            return Transaction.objects.all()  # Пока что для тестов, потом будет -> filter(user=0)
    serializer_class = TransactionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TransactionFilter
