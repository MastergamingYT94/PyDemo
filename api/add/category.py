from django.shortcuts import render
from PyCommerce.models import category
from abc import ABC, abstractmethod
from django.views.decorators.csrf import csrf_exempt


class IAddCategory(ABC):
    @abstractmethod
    def category():
        pass


class Category():
    def category(self, request):
        if request.method == "POST":
            result = category()
            result.MainCategoryId = request.POST.get("MainCategoryId")
            result.NameA = request.POST.get("NameA")
            result.NameL = request.POST.get("NameL")
            result.Level = request.POST.get("Level")
            result.ImageUrl = request.POST.get("ImageUrl")
            result.save()
            return render(request)


add_category = Category().category
