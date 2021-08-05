from django.db.models.aggregates import Sum
from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.http.response import HttpResponse
from PyCommerce.models import inventoryDetails,  inventoryBalances


class IUpdateInventoryBalance(ABC):
    @abstractmethod
    def update_inv_balance():
        pass


class UpdateInvBalance():
    @csrf_exempt
    def update_inv_balance(self, data):
        invDetail = inventoryDetails.objects.filter(
            ProductId=data["ProductId_id"], StoreId=data["StoreId_id"])
        invBalance = inventoryBalances.objects.filter(
            ProductId=data["ProductId_id"], StoreId=data["StoreId_id"])
        if invBalance.count() > 0:
            quantityIn = invDetail.filter(
                TransType_id=1).aggregate(Sum('Quantity'))
            quantityOut = invDetail.filter(
                TransType_id=2).aggregate(Sum('Quantity'))
            quantityBalance = float(
                quantityIn['Quantity__sum']) - float(quantityOut['Quantity__sum'])
            invBalance.update(QuantityBalance=quantityBalance)
        else:
            inventoryBalances.objects.create(
                ProductId_id=data["ProductId_id"], StoreId_id=data["StoreId_id"], QuantityBalance=data["Quantity"])
        return HttpResponse(True)


update_inv_balance = UpdateInvBalance().update_inv_balance
