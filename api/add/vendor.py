from abc import ABC, abstractmethod
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from PyCommerce.models import vendors


class IAddVendor(ABC):
    @abstractmethod
    def vendor():
        pass


class Vendor():
    @csrf_exempt
    def vendor(self, request):
        if request.method == "POST":
            result = vendors()
            result.NameA = request.POST.get("NameA")
            result.NameL = request.POST.get("NameL")
            result.Adress1 = request.POST.get("Adress1")
            result.Adress2 = request.POST.get("Adress2")
            result.Phone = request.POST.get("Phone")
            result.Email = request.POST.get("Email")
            result.Password = request.POST.get("Password")
            result.PostCode = request.POST.get("PostCode")
            result.save()
            return render(request)


add_vendor = Vendor().vendor
