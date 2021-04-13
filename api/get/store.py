from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import StoresResource
from PyCommerce.models import stores


class IGetStore(ABC):
    @abstractmethod
    def store():
        pass


class Store():
    def store(self, request, id):
        request.method = "GET"
        if request.method == 'GET':
            sanitizer = StoresResource(stores.objects.filter(pk=id), many=True)
            return JsonResponse(sanitizer.data, safe=False)


get_store = Store().store
