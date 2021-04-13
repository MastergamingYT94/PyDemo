from django.http.response import JsonResponse
from PyCommerce.models import products
from abc import ABC, abstractmethod


class IAddProduct(ABC):
    @abstractmethod
    def product():
        pass


class Product():
    def product(self, request):
        if request.method == "POST":
            get = request.POST.get

            products.objects.create(
                NameA=get('NameA'),
                NameL=get('NameL'),
                ImageUrl=get('ImageUrl'),
                ImageUrl6=get('ImageUrl'),
                ImageUrl7=get('ImageUrl7'),
                CategoryId=get('CategoryId'),
                BrandId=get('BrandId'),
                Description=get('Description'))
            return JsonResponse(request.POST, safe=False)


add_product = Product().product
