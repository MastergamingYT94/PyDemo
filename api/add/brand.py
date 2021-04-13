from django.http.response import JsonResponse
from PyCommerce.models import brands
from abc import ABC, abstractmethod


class IAddBrand(ABC):
    @abstractmethod
    def brand():
        pass


class Brand():
    def brand(self, request):
        if request.method == "POST":
            get = request.POST.get

            brands.objects.create(
                NameA=get('NameA'),
                NameL=get('NameL'))
            return JsonResponse(request.POST, safe=False)


add_brand = Brand().brand
