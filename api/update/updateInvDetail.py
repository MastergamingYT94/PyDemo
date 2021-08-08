from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from PyCommerce.models import inventoryDetails
from api.update.invBalance import update_inv_balance
from api.update.checkBalance import check_inv_balance
import json


class IUpdateInventoryDetail(ABC):
    @abstractmethod
    def update_inv_detail():
        pass


class UpdateInvDetail():
    @csrf_exempt
    def update_inv_detail(self, request, id):
        response = False
        if request.method == "POST":
            response = True
            data = json.loads(request.body)
            if data['TransType_id'] == 2:
                check_balance = check_inv_balance(
                    data['ProductId_id'], data['StoreId_id'], data['Quantity'], id)
                if check_balance == True:
                    inventoryDetails.objects.filter(id=id).update(**data)
                    update_inv_balance(data, id)
                else:
                    response = False
            else:
                inventoryDetails.objects.filter(id=id).update(**data)
                update_inv_balance(data)
            return JsonResponse(response, safe=False)


update_inv_detail = UpdateInvDetail().update_inv_detail
