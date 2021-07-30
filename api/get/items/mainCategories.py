from PyCommerce.models import categories
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api.resources import categoriesResource
from api.encrypt import encrypt


class IGetMainCategories(ABC):
    @abstractmethod
    def get_main_categories():
        pass


class MainCategories():
    def get_main_categories(self, request):
        if request.method == 'GET':
            data = categories.objects.filter(Level=1).order_by('id')
            Serializer = categoriesResource(data, many=True)
            return JsonResponse(encrypt(Serializer.data), safe=False)


get_main_categories = MainCategories().get_main_categories
