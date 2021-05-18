from django.shortcuts import render
from PyCommerce.models import products
from abc import ABC, abstractmethod
from django.views.decorators.csrf import csrf_exempt


class IAddProduct(ABC):
    @abstractmethod
    def product():
        pass


class Product():
    @csrf_exempt
    def product(self, request):
        if request.method == "POST":
            result = products()
            result.ImageUrl = request.POST.get("ImageUrl")
            result.ImageUrl6 = request.POST.get("ImageUrl6")
            result.ImageUrl7 = request.POST.get("ImageUrl7")
            result.CategoryId = request.POST.get("CategoryId")
            result.BrandId = request.POST.get("BrandId")
            result.Description = request.POST.get("Description")
            result.save()
            return render(request)


add_product = Product().product
