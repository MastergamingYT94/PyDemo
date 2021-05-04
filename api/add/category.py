from django.shortcuts import render
from PyCommerce.models import category
from abc import ABC, abstractmethod


class IAddBrand(ABC):
    @abstractmethod
    def category():
        pass


class Category():
    def category(self, request):
        if request.method == "POST":
            saveRecord = category()
            saveRecord.MainCategoryId = request.POST.get("MainCategoryId")
            saveRecord.NameL = request.POST.get("NameL")
            saveRecord.NameA = request.POST.get("NameA")
            saveRecord.Level = request.POST.get("Level")
            saveRecord.ImageUrl = request.POST.get("ImageUrl")
            saveRecord.save()
        return render(request)


add_category = Category().category
