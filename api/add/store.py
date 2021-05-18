from django.shortcuts import render
from PyCommerce.models import stores
from abc import ABC, abstractmethod
from django.views.decorators.csrf import csrf_exempt


class IAddStore(ABC):
    @abstractmethod
    def store():
        pass


class Store():
    @csrf_exempt
    def store(self, request):
        if request.method == "POST":
            result = stores()
            result.VendorId = request.POST.get("VendorId")
            result.NameA = request.POST.get("NameA")
            result.NameL = request.POST.get("NameL")
            result.email = request.POST.get("email")
            result.Address = request.POST.get("Address")
            result.CountryId = request.POST.get("CountryId")
            result.City = request.POST.get("City")
            result.MapLocation = request.POST.get("MapLocation")
            result.ShippingAgentId = request.POST.get("ShippingAgentId")
            result.NameL = request.POST.get("NameL")
            result.NameL = request.POST.get("NameL")
            result.save()
            return render(request)


add_store = Store().store
