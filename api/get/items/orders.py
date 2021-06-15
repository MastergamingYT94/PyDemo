from PyCommerce.models import orders, shippingAgentUsers
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api.resources import ordersResource


class IGetOrders(ABC):
    @abstractmethod
    def get_orders():
        pass


class Orders():
    def get_orders(self, request, userId):
        if request.method == 'GET':
            data = orders.objects.filter(UserId=userId)
            Serializer = ordersResource(data, many=True)
        return JsonResponse(Serializer.data, safe=False)


get_orders = Orders().get_orders
