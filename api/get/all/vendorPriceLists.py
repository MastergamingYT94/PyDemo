from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import VendorPriceListResource
from PyCommerce.models import vendorPriceList


class IGetVendorPriceList(ABC):
    @abstractmethod
    def vendor_price_list():
        pass


class VendorPriceList():
    def vendor_price_list(self, request):
        if request.method == 'GET':
            vendorPriceListSerializer = VendorPriceListResource(
                vendorPriceList.objects.all(), many=True)
            return JsonResponse(vendorPriceListSerializer.data, safe=False)


get_vendor_price_lists = VendorPriceList().vendor_price_list
