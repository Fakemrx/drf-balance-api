from django.urls import path

from transactions.views.crud import TransactionAPIRUD, TransactionAPICreate
from transactions.views.list_filter import TransactionsAPIView

urlpatterns = [
    path('list/', TransactionsAPIView.as_view(), name='list'),
    path('create/', TransactionAPICreate.as_view({'post': 'create'}), name='create'),
    path('rud/<int:pk>', TransactionAPIRUD.as_view(), name='rud'),
]