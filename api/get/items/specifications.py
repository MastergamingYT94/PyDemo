from PyCommerce.models import productSpecifications, specifications
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api.resources import SpecificationsResource
from api.encrypt import encrypt


class IGetSpecifications(ABC):
    @abstractmethod
    def get_specifications():
        pass


class Specifications():
    def get_specifications(self, request, CategoryId=None):
        if request.method == 'GET':
            data = productSpecifications.objects.filter(
                CategoryId=CategoryId, ShowInFilter=True)

            Serializer = SpecificationsResource(data, many=True)
            return JsonResponse(encrypt(Serializer.data), safe=False)


get_specifications = Specifications().get_specifications
