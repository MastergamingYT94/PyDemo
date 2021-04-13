from django.http.response import JsonResponse
from PyCommerce.models import stores
from abc import ABC, abstractmethod


class IAddStore(ABC):
    @abstractmethod
    def store():
        pass


class Store():
    def store(self, request):
        if request.method == "POST":
            get = request.POST.get

            stores.objects.create(
                VendorId=get('VendorId'),
                NameA=get('NameA'),
                NameL=get('NameL'),
                email=get('email'),
                Address=get('Address'),
                CountryId=get('CountryId'),
                City=get('City'),
                MapLocation=get('MapLocation'),
                ShippingAgentId=get('ShippingAgentId'))
            return JsonResponse(request.POST, safe=False)


add_store = Store().store
