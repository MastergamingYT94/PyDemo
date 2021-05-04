from django.shortcuts import render
from PyCommerce.models import vendorPriceList
from abc import ABC, abstractmethod


class IAddPriceList(ABC):
    @abstractmethod
    def price_list():
        pass


class PriceList():
    def price_list(self, request):
        if request.method == "POST":
            saveRecord = vendorPriceList()
            saveRecord.VendorId = request.POST.get("VendorId")
            saveRecord.ProductId = request.POST.get("ProductId")
            saveRecord.CountryId = request.POST.get("CountryId")
            saveRecord.Price = request.POST.get("Price")
            saveRecord.save()
        return render(request)


add_price_list = PriceList().price_list
