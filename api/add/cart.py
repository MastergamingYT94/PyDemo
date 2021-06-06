from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.http.response import HttpResponse, JsonResponse
from PyCommerce.models import cartTransactionMasters
import datetime


class IAddCartMaster(ABC):
    @abstractmethod
    def add_cart_master():
        pass


class CartMaster():
    @csrf_exempt
    def add_cart_master(self, request):
        if request.method == "GET":
            DateCreated = datetime.datetime.now()
            data = cartTransactionMasters.objects.create(
                DateCreated=DateCreated)
            return JsonResponse(data.id, safe=False)


add_cart_master = CartMaster().add_cart_master
