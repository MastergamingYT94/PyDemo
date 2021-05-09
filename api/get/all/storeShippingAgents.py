from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import StoreShippingAgentResource
from PyCommerce.models import storeShippingAgent


class IGetStoreShippingAgent(ABC):
    @abstractmethod
    def store_shipping_agents():
        pass


class StoreShippingAgent():
    def store_shipping_agents(self, request):
        if request.method == 'GET':
            storeShippingSerializer = StoreShippingAgentResource(
                storeShippingAgent.objects.all(), many=True)
            return JsonResponse(storeShippingSerializer.data, safe=False)


get_store_shipping_agents = StoreShippingAgent().store_shipping_agents
