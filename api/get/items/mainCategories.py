from PyCommerce.models import categories
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api.resources import categoriesResource


class IGetMainCategories(ABC):
    @abstractmethod
    def get_main_categories():
        pass


class MainCategories():
    def get_main_categories(self, request):
        if request.method == 'GET':
            data = categories.objects.filter(Level=1)
            Serializer = categoriesResource(data, many=True)
            return JsonResponse(Serializer.data, safe=False)


get_main_categories = MainCategories().get_main_categories
