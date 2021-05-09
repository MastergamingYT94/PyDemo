from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import OrderStatusResource
from PyCommerce.models import orderStatus


class IGetOrderStatus(ABC):
    @abstractmethod
    def order_status():
        pass


class OrderStatus():
    def order_status(self, request):
        if request.method == 'GET':
            orderStatusSerializer = OrderStatusResource(
                orderStatus.objects.all(), many=True)
            return JsonResponse(orderStatusSerializer.data, safe=False)


get_order_status = OrderStatus().order_status
