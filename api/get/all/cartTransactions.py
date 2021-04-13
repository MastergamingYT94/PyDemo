from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from PyCommerce.models import cartTransaction
from api.models import CartTransactionResource


class IGetCartTransaction(ABC):
    @abstractmethod
    def cart_transaction():
        pass


class CartTransaction():
    def cart_transaction(self, request):
        if request.method == 'GET':
            sanitizer = CartTransactionResource(
                cartTransaction.objects.all(), many=True)
            return JsonResponse(sanitizer.data, safe=False)


get_cart_transactions = CartTransaction().cart_transaction
