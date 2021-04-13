from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import CartTransactionMasterResource
from PyCommerce.models import cartTransactionMaster


class IGetCartTransactionMaster(ABC):
    @abstractmethod
    def cart_transaction_master():
        pass


class CartTransactionMaster():
    def cart_transaction_master(self, request):
        if request.method == 'GET':
            sanitizer = CartTransactionMasterResource(
                cartTransactionMaster.objects.all(), many=True)
            return JsonResponse(sanitizer.data, safe=False)


get_cart_transaction_masters = CartTransactionMaster().cart_transaction_master
