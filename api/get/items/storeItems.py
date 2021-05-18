from django.http.response import JsonResponse
from PyCommerce.models import stores, vendors, shippingAgent


def vendorName():
    Stores = stores.objects.all()
    storesIds = [item.VendorId for item in Stores]

    items = vendors.objects.all().filter(Id__in=storesIds)
    Name = [item.NameL for item in items]
    for item in Name:
        return item


def shippingAgentName():
    Stores = stores.objects.all()
    storesIds = [Id.ShippingAgentId for Id in Stores]

    data = shippingAgent.objects.all().filter(Id__in=storesIds)
    Name = [item for item in data]
    for item in Name:
        return item.NameL
