from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import CategoryResource
from PyCommerce.models import category


class IGetCategories(ABC):
    @abstractmethod
    def categories():
        pass


class Categories():
    def categories(self, request):
        if request.method == 'GET':
            cartegorySerializer = CategoryResource(
                category.objects.all(), many=True)
            return JsonResponse(cartegorySerializer.data, safe=False)


get_categories = Categories().categories
