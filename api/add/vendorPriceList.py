from django.http.response import JsonResponse
from PyCommerce.models import vendorPriceList
from abc import ABC, abstractmethod


class IAddPriceList(ABC):
    @abstractmethod
    def price_list():
        pass


class PriceList():
    def price_list(self, request):
        if request.method == "POST":
            get = request.POST.get

            vendorPriceList.objects.create(
                VendorId=get('VendorId'),
                ProductId=get('ProductId'),
                CountryId=get('CountryId'),
                Price=get('Price')
            )
            return JsonResponse(request.POST, safe=False)


add_price_list = PriceList().price_list
