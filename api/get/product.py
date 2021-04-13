from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import ProductsResource
from PyCommerce.models import products


class IGetProduct(ABC):
    @abstractmethod
    def product():
        pass


class Product():
    def product(self, request, id):
        request.method = "GET"
        if request.method == 'GET':
            sanitizer = ProductsResource(
                products.objects.filter(pk=id), many=True)
            return JsonResponse(sanitizer.data, safe=False)


get_product = Product().product
