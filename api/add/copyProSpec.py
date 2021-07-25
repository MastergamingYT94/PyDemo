from PyCommerce.models import productSpecifications
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod


class ICopyProductSpecifications(ABC):
    @abstractmethod
    def copy_product_specifications():
        pass


class CopyProductSpecifications():
    @csrf_exempt
    def copy_product_specifications(self, request, ProductSpecId, ProductId, CategoryId):
        if request.method == 'POST':
            specifications = [item for item in productSpecifications.objects.filter(
                ProductId=ProductSpecId)]
            for item in specifications:
                check = productSpecifications.objects.filter(
                    ProductId=ProductId, SpecificationId=item.SpecificationId.id)
                if check.count() == 0:
                    productSpecifications.objects.create(
                        ProductId=ProductId, SpecificationId=item.SpecificationId.id, SpecificationValue=item.SpecificationValue, CategoryId=CategoryId)
        return JsonResponse(True, safe=False)


copy_product_specifications = CopyProductSpecifications().copy_product_specifications
