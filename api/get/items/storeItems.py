from django.http.response import JsonResponse
from PyCommerce.models import Stores, Vendors, ShippingAgents


def vendorName():
    Stores = Stores.objects.all()
    storesIds = [item.VendorId for item in Stores]

    items = Vendors.objects.all().filter(Id__in=storesIds)
    Name = [item.NameL for item in items]
    for item in Name:
        return item


def shippingAgentName():
    Stores = Stores.objects.all()
    storesIds = [Id.ShippingAgentId for Id in Stores]

    data = ShippingAgents.objects.all().filter(Id__in=storesIds)
    Name = [item for item in data]
    for item in Name:
        return item.NameL
