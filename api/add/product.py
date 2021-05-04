from django.shortcuts import render
from PyCommerce.models import products
from abc import ABC, abstractmethod


class IAddProduct(ABC):
    @abstractmethod
    def product():
        pass


class Product():
    def product(self, request):
        if request.method == "POST":
            saveRecord = products()
            saveRecord.NameA = request.POST.get("NameA")
            saveRecord.NameL = request.POST.get("NameL")
            saveRecord.ImageUrl = request.POST.get("ImageUrl")
            saveRecord.ImageUrl6 = request.POST.get("ImageUrl6")
            saveRecord.ImageUrl7 = request.POST.get("ImageUrl7")
            saveRecord.CategoryId = request.POST.get("CategoryId")
            saveRecord.BrandId = request.POST.get("BrandId")
            saveRecord.Description = request.POST.get("Description")
            saveRecord.save()
        return render(request)


add_product = Product().product
