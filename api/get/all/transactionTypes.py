from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import TransactionTypeResource
from PyCommerce.models import transactionType


class IGetTransactionType(ABC):
    @abstractmethod
    def transaction_type():
        pass


class TransactionType():
    def transaction_type(self, request):
        if request.method == 'GET':
            transactionTypeSerializer = TransactionTypeResource(
                transactionType.objects.all(), many=True)
            return JsonResponse(transactionTypeSerializer.data, safe=False)


get_transaction_types = TransactionType().transaction_type
