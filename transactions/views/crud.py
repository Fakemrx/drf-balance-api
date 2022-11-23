from rest_framework import generics, mixins, viewsets, response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from category.models import UserCategories
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer, TransactionRUDSerializer


class TransactionAPICreate(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if user:
            serializer.save(user=user)


class TransactionAPIRUD(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = TransactionRUDSerializer
    queryset = Transaction.objects.all()
