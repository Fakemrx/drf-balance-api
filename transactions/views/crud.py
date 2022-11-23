from rest_framework import generics, mixins, viewsets, response, status
from rest_framework.response import Response

from category.models import UserCategories
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class TransactionAPIRetrieveCreate(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if user:
            serializer.save(user=user)


class TransactionAPIRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
