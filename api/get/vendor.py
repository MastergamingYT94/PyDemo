from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import VendorsResource
from PyCommerce.models import vendors


class IGetVendor(ABC):
    @abstractmethod
    def vendor():
        pass


class Vendor():
    def vendor(self, request, id):
        request.method = "GET"
        if request.method == 'GET':
            vendorSerializer = VendorsResource(
                vendors.objects.filter(pk=id), many=True)
            return JsonResponse(vendorSerializer.data, safe=False)


get_vendor = Vendor().vendor
