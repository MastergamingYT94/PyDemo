from django.shortcuts import render
from PyCommerce.models import brands
from abc import ABC, abstractmethod
from django.views.decorators.csrf import csrf_exempt


class IAddBrand(ABC):
    @abstractmethod
    def brand():
        pass


class Brand():
    @csrf_exempt
    def brand(self, request):
        if request.method == "POST":
            result = brands()
            result.NameA = request.POST.get("NameA")
            result.NameL = request.POST.get("NameL")
            result.save()
            return render(request)


add_brand = Brand().brand
