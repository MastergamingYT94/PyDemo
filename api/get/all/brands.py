from PyCommerce.models import brands
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api.models import BrandsResource


class IGetBrands(ABC):
    @abstractmethod
    def brands():
        pass


class Brands():
    def brands(self, request):
        if request.method == 'GET':
            brandSerializer = BrandsResource(brands.objects.all(), many=True)
            return JsonResponse(brandSerializer.data, safe=False)


get_brands = Brands().brands
