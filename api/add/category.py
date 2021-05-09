from django.http.response import JsonResponse
from PyCommerce.models import category
from abc import ABC, abstractmethod


class IAddBrand(ABC):
    @abstractmethod
    def category():
        pass


class Category():
    def category(self, request):
        if request.method == "POST":
            get = request.POST.get

            category.objects.create(
                MainCategoryId=get('MainCategoryId'),
                NameA=get('NameA'),
                NameL=get('NameL'),
                Level=get('Level'),
                ImageUrl=get('ImageUrl'),
            )
            return JsonResponse(request.POST, safe=False)


add_category = Category().category
