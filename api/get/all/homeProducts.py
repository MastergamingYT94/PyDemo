from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import GetHomeProductsResource
from PyCommerce.models import getHomeProducts
import math


class IGetHomeProducts(ABC):
    @abstractmethod
    def get_home_products():
        pass

    def max_page():
        pass


class GetHomeProducts(IGetHomeProducts):
    def get_home_products(self, request):
        if request.method == 'GET':
            sanitizer = GetHomeProductsResource(
                getHomeProducts.objects.all().order_by('StoreId'), many=True)
            return JsonResponse(sanitizer.data, safe=False)

    def max_page(self, request):
        if request.method == 'GET':
            Products = getHomeProducts.objects.all().order_by("StoreId")
            maxPageNumber = len(Products) / 8
            maxPageNumber = math.ceil(maxPageNumber) * 10
            return JsonResponse(maxPageNumber, safe=False)


get_home_products = GetHomeProducts().get_home_products
get_max_page = GetHomeProducts().max_page
