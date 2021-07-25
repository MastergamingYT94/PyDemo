from PyCommerce.models import productSpecifications
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api.resources import productSpecificationsResource


class IGetProductSpecifications(ABC):
    @abstractmethod
    def get_product_specifications():
        pass


class ProductSpecifications():
    def get_product_specifications(self, request, ProductId):
        if request.method == 'GET':
            data = productSpecifications.objects.filter(ProductId=ProductId)
            Serializer = productSpecificationsResource(data, many=True)
            return JsonResponse(Serializer.data, safe=False)


get_product_specifications = ProductSpecifications().get_product_specifications
