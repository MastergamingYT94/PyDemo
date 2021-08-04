from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.core.files.base import ContentFile
from django.http.response import HttpResponse
from PyCommerce.models import products


class IUpdateProduct(ABC):
    @abstractmethod
    def update():
        pass


class updateProduct():
    @csrf_exempt
    def update(self, request, id):
        product = products.objects.get(id=id)
        img = request.FILES.get('Image')
        img2 = request.FILES.get('Image2')
        img3 = request.FILES.get('Image3')
        img4 = request.FILES.get('Image4')
        if img:
            file_content = ContentFile(img.read())
            product.Image.save(img.name, file_content)
            product.save()
        if img2:
            file_content = ContentFile(img2.read())
            product.Image2.save(img2.name, file_content)
            product.save()
        if img3:
            file_content = ContentFile(img3.read())
            product.Image3.save(img3.name, file_content)
            product.save()
        if img4:
            file_content = ContentFile(img4.read())
            product.Image4.save(img4.name, file_content)
            product.save()
        name = request.POST['NameL']
        brand = request.POST['BrandId']
        category = request.POST['CategoryId']
        description = request.POST['Description']
        products.objects.filter(id=id).update(
            NameL=name, BrandId=brand, CategoryId=category, Description=description)
        return HttpResponse(request)


update_product = updateProduct().update
