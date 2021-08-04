from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.http.response import HttpResponse
from PyCommerce.models import inventoryDetails
from api.update.invBalance import update_inv_balance
import json


class IAddInventoryDetail(ABC):
    @abstractmethod
    def add_inv_detail():
        pass


class addInvDetail():
    @csrf_exempt
    def add_inv_detail(self, request):
        if request.method == "POST":
            data = json.loads(request.body)
            inventoryDetails.objects.create(**data)
            update_inv_balance(data)
            return HttpResponse(request)


add_inv_detail = addInvDetail().add_inv_detail
