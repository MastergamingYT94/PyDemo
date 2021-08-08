from django.db.models.aggregates import Sum
from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from PyCommerce.models import inventoryDetails,  inventoryBalances


class ICheckInventoryBalance(ABC):
    @abstractmethod
    def check_inv_balance():
        pass


class CheckInvBalance():
    @csrf_exempt
    def check_inv_balance(self, ProductId, StoreId, Quantity, id=0):
        invDetail = inventoryDetails.objects.filter(
            ProductId=ProductId, StoreId=StoreId)
        if id > 0:
            invDetail = invDetail.exclude(id=id)
        quantityIn = invDetail.filter(
            TransType_id=1).aggregate(Sum('Quantity'))
        quantityOut = invDetail.filter(
            TransType_id=2).aggregate(Sum('Quantity'))
        if quantityIn['Quantity__sum'] != None:
            quantityIn = float(quantityIn['Quantity__sum'])
        else:
            quantityIn = 0

        if quantityOut['Quantity__sum'] != None:
            quantityOut = float(quantityOut['Quantity__sum'])
        else:
            quantityOut = 0

        quantityBalance = (quantityIn - quantityOut) - float(Quantity)
        if quantityBalance < 0:
            return False
        else:
            return True


check_inv_balance = CheckInvBalance().check_inv_balance
