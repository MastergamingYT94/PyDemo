from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import InventoryDetailResource
from PyCommerce.models import inventoryDetail


class IGetInventoryDetail(ABC):
    @abstractmethod
    def inventory_detail():
        pass


class InventoryDetail():
    def inventory_detail(self, request):
        if request.method == 'GET':
            sanitizer = InventoryDetailResource(
                inventoryDetail.objects.all(), many=True)
            return JsonResponse(sanitizer.data, safe=False)


get_inventory_details = InventoryDetail().inventory_detail
