from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import VendorsResource
from PyCommerce.models import vendors


class IGetVendors(ABC):
    @abstractmethod
    def vendors():
        pass


class Vendors():
    def vendors(self, request):
        if request.method == 'GET':
            vendorSerializer = VendorsResource(
                vendors.objects.all(), many=True)
            return JsonResponse(vendorSerializer.data, safe=False)


get_vendors = Vendors().vendors
