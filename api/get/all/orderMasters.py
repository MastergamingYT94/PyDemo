from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import OrderMasterResource
from PyCommerce.models import orderMaster


class IGetOrderMaster(ABC):
    @abstractmethod
    def order_master():
        pass


class OrderMaster():
    def order_master(self, request):
        if request.method == 'GET':
            orderMasterSerializer = OrderMasterResource(
                orderMaster.objects.all(), many=True)
            return JsonResponse(orderMasterSerializer.data, safe=False)


get_order_masters = OrderMaster().order_master
