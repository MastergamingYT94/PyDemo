from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import InventoryBalanceResource
from PyCommerce.models import inventoryBalance


class IGetInventoryBalance(ABC):
    @abstractmethod
    def inventory_balance():
        pass


class InventoryBalance():
    def inventory_balance(self, request):
        if request.method == 'GET':
            sanitizer = InventoryBalanceResource(
                inventoryBalance.objects.all(), many=True)
            return JsonResponse(sanitizer.data, safe=False)


get_inventory_balances = InventoryBalance().inventory_balance
