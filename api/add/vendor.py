from django.http.response import JsonResponse
from PyCommerce.models import vendors
from abc import ABC, abstractmethod


class IAddVendor(ABC):
    @abstractmethod
    def vendor():
        pass


class Vendor():
    def vendor(self, request):
        if request.method == "POST":
            get = request.POST.get

            vendors.objects.create(
                NameA=get('NameA'),
                NameL=get('NameL'),
                Adress1=get('Adress1'),
                Adress2=get('Adress2'),
                Phone=get('Phone'),
                Email=get('Email'),
                Password=get('Password'),
                PostCode=get('PostCode'),
            )
            return JsonResponse(request.POST, safe=False)


add_vendor = Vendor().vendor
