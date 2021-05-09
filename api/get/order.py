from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import OrdersResource
from PyCommerce.models import orders


class IGetOrder(ABC):
    @abstractmethod
    def order():
        pass


class Order():
    def order(self, request, id):
        request.method = "GET"
        if request.method == 'GET':
            orderSerializer = OrdersResource(
                orders.objects.filter(pk=id), many=True)
            return JsonResponse(orderSerializer.data, safe=False)


get_order = Order().order
