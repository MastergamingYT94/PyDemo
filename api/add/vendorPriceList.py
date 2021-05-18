from django.shortcuts import render
from PyCommerce.models import vendorPriceList
from abc import ABC, abstractmethod
from django.views.decorators.csrf import csrf_exempt


class IAddPriceList(ABC):
    @abstractmethod
    def price_list():
        pass


class PriceList():
    @csrf_exempt
    def price_list(self, request):
        if request.method == "POST":
            result = vendorPriceList()
            result.VendorId = request.POST.get("VendorId")
            result.ProductId = request.POST.get("ProductId")
            result.CountryId = request.POST.get("CountryId")
            result.Price = request.POST.get("Price")
            result.save()
            return render(request)


add_price_list = PriceList().price_list
