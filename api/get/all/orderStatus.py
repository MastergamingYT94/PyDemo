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
            sanitizer = OrderStatusResource(
                orderStatus.objects.all(), many=True)
            return JsonResponse(sanitizer.data, safe=False)


get_order_status = OrderStatus().order_status
