from PyCommerce.models import categories
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api.resources import categoriesResource
from api.encrypt import encrypt


class IGetSubCategories(ABC):
    @abstractmethod
    def get_sub_categories():
        pass


class SubCategories():
    def get_sub_categories(self, request):
        if request.method == 'GET':
            data = categories.objects.filter(Level=2)
            Serializer = categoriesResource(data, many=True)
            return JsonResponse(encrypt(Serializer.data), safe=False)


get_sub_categories = SubCategories().get_sub_categories
