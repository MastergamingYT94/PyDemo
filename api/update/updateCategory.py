from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.core.files.base import ContentFile
from django.http.response import HttpResponse
from PyCommerce.models import categories


class IUpdateCategory(ABC):
    @abstractmethod
    def update_category():
        pass


class updateCategory():
    @csrf_exempt
    def update_category(self, request, id):
        category = categories.objects.get(id=id)
        img = request.FILES.get('Image')
        if img:
            file_content = ContentFile(img.read())
            category.ImageUrl.save(img.name, file_content)
            category.save()
        name = request.POST['NameL']
        mainCategory = request.POST['MainCategoryId']
        categories.objects.filter(id=id).update(
            NameL=name, MainCategoryId_id=mainCategory)
        return HttpResponse(request)


update_category = updateCategory().update_category
