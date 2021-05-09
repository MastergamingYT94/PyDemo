from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import ProductSpecificationsResource
from PyCommerce.models import productSpecifications


class IGetProductSpecifications(ABC):
    @abstractmethod
    def product_specifications():
        pass


class ProductSpecifications():
    def product_specifications(self, request):
        if request.method == 'GET':
            productSpecificationSerializer = ProductSpecificationsResource(
                productSpecifications.objects.all(), many=True)
            return JsonResponse(productSpecificationSerializer.data, safe=False)


get_product_specifications = ProductSpecifications().product_specifications
