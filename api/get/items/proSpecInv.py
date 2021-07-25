from PyCommerce.models import inventoryBalances, productSpecifications
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api.resources import productSpecificationsInvResource


class IGetProductSpecFromInv(ABC):
    @abstractmethod
    def get_product_specifications_inv():
        pass


class ProductSpecifications():
    def get_product_specifications_inv(self, request, ProductId=None):
        if request.method == 'GET':
            items = inventoryBalances.objects.filter(
                id=ProductId)
            items = [item.ProductId for item in items]
            data = productSpecifications.objects.filter(ProductId__in=items)

            Serializer = productSpecificationsInvResource(
                data, many=True)
            return JsonResponse(Serializer.data, safe=False)


get_product_specifications_inv = ProductSpecifications().get_product_specifications_inv
