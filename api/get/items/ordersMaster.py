from PyCommerce.models import orderMasters
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api.resources import orderMastersResource


class IGetOrders(ABC):
    @abstractmethod
    def get_orders_master():
        pass


class OrdersMaster():
    def get_orders_master(self, request, UserId):
        if request.method == 'GET':
            data = orderMasters.objects.filter(UserId=UserId)
            Serializer = orderMastersResource(data, many=True)
        return JsonResponse(Serializer.data, safe=False)


get_orders_master = OrdersMaster().get_orders_master
