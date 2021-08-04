from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.core.files.base import ContentFile
from django.http.response import HttpResponse
from PyCommerce.models import categories


class IAddCategory(ABC):
    @abstractmethod
    def add_category():
        pass


class AddCategory():
    @csrf_exempt
    def add_category(self, request):
        name = request.POST['NameL']
        MainCategory = request.POST['MainCategoryId']
        category = categories.objects.create(
            NameL=name, MainCategoryId_id=MainCategory)
        category = categories.objects.get(id=category.id)
        img = request.FILES.get('ImageUrl')
        if img:
            file_content = ContentFile(img.read())
            category.ImageUrl.save(img.name, file_content)
            category.save()
        return HttpResponse(request)


add_category = AddCategory().add_category
