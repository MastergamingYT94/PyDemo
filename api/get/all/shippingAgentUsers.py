from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import ShippingAgentUserResource
from PyCommerce.models import shippingAgentUser


class IGetShippingAgentUser(ABC):
    @abstractmethod
    def shipping_agent_user():
        pass


class ShippingAgentUser():
    def shipping_agent_user(self, request):
        if request.method == 'GET':
            sanitizer = ShippingAgentUserResource(
                shippingAgentUser.objects.all(), many=True)
            return JsonResponse(sanitizer.data, safe=False)


get_shipping_agent_users = ShippingAgentUser().shipping_agent_user
