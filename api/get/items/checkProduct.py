from PyCommerce.models import stores, vendorPriceLists
from django.http.response import JsonResponse
from abc import ABC, abstractmethod


class ICheckProductExists(ABC):
    @abstractmethod
    def check_product_exists():
        pass


class CheckProduct():
    def check_product_exists(self, request, StoreId, ProductId):
        if request.method == 'GET':
            vendor = [
                item.VendorId.id for item in stores.objects.filter(id=StoreId)]
            check = vendorPriceLists.objects.filter(
                ProductId=ProductId, VendorId__in=vendor)
            if check.count() > 0:
                return JsonResponse(True, safe=False)
        return JsonResponse(False, safe=False)


check_product_exists = CheckProduct().check_product_exists
