from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import OrdersResource
from PyCommerce.models import orders


class IGetOrders(ABC):
    @abstractmethod
    def orders():
        pass


class Orders():
    def orders(self, request):
        if request.method == 'GET':
            sanitizer = OrdersResource(orders.objects.all(), many=True)
            return JsonResponse(sanitizer.data, safe=False)


get_orders = Orders().orders
