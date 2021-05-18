from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import StoresResource
from PyCommerce.models import stores


class IGetStores(ABC):
    @abstractmethod
    def stores():
        pass


class Stores():
    def stores(self, request):
        if request.method == 'GET':

            storeSerializer = StoresResource(stores.objects.all(), many=True)
            return JsonResponse(storeSerializer.data, safe=False)


get_stores = Stores().stores
