from PyCommerce.models import brands
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api.models import BrandsResource


class IGetBrand(ABC):
    @abstractmethod
    def brand():
        pass


class Brand():
    def brand(self, request, id):
        request.method = "GET"
        if request.method == 'GET':
            sanitizer = BrandsResource(brands.objects.filter(pk=id), many=True)
            return JsonResponse(sanitizer.data, safe=False)


get_brand = Brand().brand
