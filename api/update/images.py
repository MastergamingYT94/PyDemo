from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.http.response import HttpResponse
from PyCommerce.models import products
import json


class IUpdateImages(ABC):
    @abstractmethod
    def update_images():
        pass


class updateImages():
    @csrf_exempt
    def update_images(self, request, id):
        if request.method == "POST":
            data = json.loads(request.body)
            products.objects.filter(id=id).update(**data)
            return HttpResponse(request)


update_images = updateImages().update_images
