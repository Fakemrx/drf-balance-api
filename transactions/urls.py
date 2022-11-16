from django.urls import path

from transactions.views.crud import TransactionAPICreate, TransactionAPIRUD
from transactions.views.list_filter import TransactionsAPIView

urlpatterns = [
    path('list/', TransactionsAPIView.as_view(), name='list'),
    path('create/', TransactionAPICreate.as_view(), name='create'),
    path('rud/<int:pk>', TransactionAPIRUD.as_view(), name='rud'),
]