from PyCommerce.models import shippingAgentUsers, shippingDetails
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api.resources import shippingDetailsResource


class IGetShippingDetails(ABC):
    @abstractmethod
    def get_shipping_details():
        pass


class ShippingDetails():
    def get_shipping_details(self, request, UserId):
        if request.method == 'GET':
            result = False
            users = shippingAgentUsers.objects.filter(UserId=UserId)
            data = shippingDetails.objects.filter(ShippingAgentId_id__in=[
                user.ShippingAgentId.id for user in users])
            if data.count() > 0:
                result = shippingDetailsResource(data, many=True).data
        return JsonResponse(result, safe=False)


get_shipping_details = ShippingDetails().get_shipping_details
