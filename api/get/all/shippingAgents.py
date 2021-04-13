from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import ShippingAgentResource
from PyCommerce.models import shippingAgent


class IGetShippingAgent(ABC):
    @abstractmethod
    def shipping_agent():
        pass


class ShippingAgent():
    def shipping_agent(self, request):
        if request.method == 'GET':
            sanitizer = ShippingAgentResource(
                shippingAgent.objects.all(), many=True)
            return JsonResponse(sanitizer.data, safe=False)


get_shipping_agents = ShippingAgent().shipping_agent
