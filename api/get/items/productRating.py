from PyCommerce.models import inventoryBalances, starPercent
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api.resources import starPercentResource


class IGetProductRating(ABC):
    @abstractmethod
    def get_product_rating():
        pass


class ProductRating():
    def get_product_rating(self, request, ProductId=None):
        if request.method == 'GET':
            items = inventoryBalances.objects.filter(
                id=ProductId)
            product = [item.ProductId.id for item in items]
            store = [item.StoreId.id for item in items]
            data = starPercent.objects.filter(
                ProductId__in=product, StoreId__in=store)

            Serializer = starPercentResource(
                data, many=True)
            data = {k: v for item in Serializer.data for k,
                    v in item.items()}
            return JsonResponse(data, safe=False)


get_product_rating = ProductRating().get_product_rating
