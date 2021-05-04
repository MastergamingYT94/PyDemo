from django.shortcuts import render
from PyCommerce.models import stores
from abc import ABC, abstractmethod


class IAddStore(ABC):
    @abstractmethod
    def store():
        pass


class Store():
    def store(self, request):
        if request.method == "POST":
            saveRecord = stores()
            saveRecord.VendorId = request.POST.get("VendorId")
            saveRecord.NameA = request.POST.get("NameA")
            saveRecord.NameL = request.POST.get("NameL")
            saveRecord.email = request.POST.get("email")
            saveRecord.Address = request.POST.get("Address")
            saveRecord.CountryId = request.POST.get("CountryId")
            saveRecord.City = request.POST.get("City")
            saveRecord.MapLocation = request.POST.get("MapLocation")
            saveRecord.ShippingAgentId = request.POST.get("ShippingAgentId")
            saveRecord.save()
        return render(request)


add_store = Store().store
