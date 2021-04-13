from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import ProductStoreRatingResource
from PyCommerce.models import productStoreRating


class IGetProductStoreRating(ABC):
    @abstractmethod
    def product_store_rating():
        pass


class ProductStoreRating():
    def product_store_rating(self, request):
        if request.method == 'GET':
            sanitizer = ProductStoreRatingResource(
                productStoreRating.objects.all(), many=True)
            return JsonResponse(sanitizer.data, safe=False)


get_product_store_ratings = ProductStoreRating().product_store_rating
