from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.http.response import HttpResponse
from PyCommerce.models import inventoryDetails
from api.update.invBalance import update_inv_balance
from api.update.checkBalance import check_inv_balance
import json


class IAddInventoryDetail(ABC):
    @abstractmethod
    def add_inv_detail():
        pass


class addInvDetail():
    @csrf_exempt
    def add_inv_detail(self, request):
        response = False
        if request.method == "POST":
            response = True
            data = json.loads(request.body)
            if data['TransType_id'] == "2":
                check_balance = check_inv_balance(
                    data['ProductId_id'], data['StoreId_id'], data['Quantity'])
                if check_balance == True:
                    inventoryDetails.objects.create(**data)
                    update_inv_balance(data)
                else:
                    response = False
            else:
                inventoryDetails.objects.create(**data)
                update_inv_balance(data)
            return HttpResponse(response)


add_inv_detail = addInvDetail().add_inv_detail
