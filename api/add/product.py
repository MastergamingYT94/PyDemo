from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.core.files.base import ContentFile
from django.http.response import HttpResponse
from PyCommerce.models import products


class IAddProduct(ABC):
    @abstractmethod
    def add_product():
        pass


class AddProduct():
    @csrf_exempt
    def add_product(self, request):
        name = request.POST['NameL']
        brand = request.POST['BrandId']
        category = request.POST['CategoryId']
        description = request.POST['Description']
        product = products.objects.create(
            NameL=name, BrandId_id=brand, CategoryId_id=category, Description=description)

        img = request.FILES.get('Image')
        img2 = request.FILES.get('Image2')
        img3 = request.FILES.get('Image3')
        img4 = request.FILES.get('Image4')
        product = products.objects.get(id=product.id)
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
        return HttpResponse(request)


add_product = AddProduct().add_product
