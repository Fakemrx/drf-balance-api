from rest_framework import generics

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class TransactionAPICreate(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class TransactionAPIRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
