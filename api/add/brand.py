from django.shortcuts import render
from PyCommerce.models import brands
from abc import ABC, abstractmethod


class IAddBrand(ABC):
    @abstractmethod
    def brand():
        pass


class Brand():
    def brand(self, request):
        if request.method == "POST":
            saveRecord = brands()
            saveRecord.NameA = request.POST.get("NameA")
            saveRecord.NameL = request.POST.get("NameL")
            saveRecord.save()
        return render(request)


add_brand = Brand().brand
