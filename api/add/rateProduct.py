import json
from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from PyCommerce.models import productStoreRatings, users


class IRateProduct(ABC):
    @abstractmethod
    def rate_product():
        pass


class RateProduct():
    @csrf_exempt
    def rate_product(self, request):
        if request.method == "POST":
            data = json.loads(request.body)
            rating = productStoreRatings.objects.filter(
                ProductId_id=data['ProductId'], StoreId_id=data['StoreId'], UserId_id=data['UserId'])
            if rating.count() > 0:
                rating.update(RatingId=data['Rating'],
                              ProductReview=data['Review'])
            else:
                productStoreRatings.objects.create(
                    ProductId_id=data['ProductId'], StoreId_id=data['StoreId'], UserId_id=data['UserId'], RatingId=data['Rating'], ProductReview=data['Review'])
        return JsonResponse(True, safe=False)


rate_product = RateProduct().rate_product
