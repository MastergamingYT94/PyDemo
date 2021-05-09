from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import ProductsResource
from PyCommerce.models import products


class IGetProducts(ABC):
    @abstractmethod
    def products():
        pass


class Products():
    def products(self, request):
        if request.method == 'GET':
            productSerializer = ProductsResource(
                products.objects.all(), many=True)
            return JsonResponse(productSerializer.data, safe=False)


get_products = Products().products
