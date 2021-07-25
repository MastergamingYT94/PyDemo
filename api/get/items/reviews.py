from PyCommerce.models import inventoryBalances, productStoreRatings
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api.resources import productStoreRatingsResource


class IGetReviews(ABC):
    @abstractmethod
    def get_reviews():
        pass


class Reviews():
    def get_reviews(self, request, ProductId=None):
        if request.method == 'GET':
            items = inventoryBalances.objects.filter(
                id=ProductId)
            product = [item.ProductId.id for item in items]
            store = [item.StoreId.id for item in items]
            data = productStoreRatings.objects.filter(
                ProductId__in=product, StoreId__in=store)
            Serializer = productStoreRatingsResource(data, many=True)
            return JsonResponse(Serializer.data, safe=False)


get_reviews = Reviews().get_reviews
