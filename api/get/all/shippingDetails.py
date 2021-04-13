from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import ShippingDetailsResource
from PyCommerce.models import shippingDetails


class IGetShippingDetails(ABC):
    @abstractmethod
    def shipping_details():
        pass


class ShippingDetails():
    def shipping_details(self, request):
        if request.method == 'GET':
            sanitizer = ShippingDetailsResource(
                shippingDetails.objects.all(), many=True)
            return JsonResponse(sanitizer.data, safe=False)


get_shipping_details = ShippingDetails.shipping_details
