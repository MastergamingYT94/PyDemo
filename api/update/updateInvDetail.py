from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.http.response import HttpResponse
from PyCommerce.models import inventoryDetails
from api.update.invBalance import update_inv_balance
import json


class IUpdateInventoryDetail(ABC):
    @abstractmethod
    def update_inv_detail():
        pass


class UpdateInvDetail():
    @csrf_exempt
    def update_inv_detail(self, request, id):
        if request.method == "POST":
            data = json.loads(request.body)
            inventoryDetails.objects.filter(id=id).update(**data)
            update_inv_balance(data)
            return HttpResponse(request)


update_inv_detail = UpdateInvDetail().update_inv_detail
