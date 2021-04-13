from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import CategoryResource
from PyCommerce.models import category


class IGetCategory(ABC):
    @abstractmethod
    def category():
        pass


class Category():
    def category(self, request, id):
        request.method = "GET"
        if request.method == 'GET':
            sanitizer = CategoryResource(
                category.objects.filter(pk=id), many=True)
            return JsonResponse(sanitizer.data, safe=False)


get_category = Category().category
