from PyCommerce.models import inventoryBalances
from django.http.response import HttpResponse
from django.db.models.aggregates import Sum
from abc import ABC, abstractmethod


class ICheckProductQuantity(ABC):
    @abstractmethod
    def check_product_quantity():
        pass


class checkProductQuantity():
    def check_product_quantity(self, request, StoreId, ProductId):
        if request.method == 'GET':
            data = inventoryBalances.objects.filter(
                StoreId_id=StoreId, ProductId_id=ProductId)
            if data.count() > 0:
                Quantity = data.aggregate(Sum('QuantityBalance'))
                Quantity = Quantity['QuantityBalance__sum']
            else:
                Quantity = 0
            return HttpResponse(Quantity)


check_product_quantity = checkProductQuantity().check_product_quantity
