from PyCommerce.models import orders, shippingAgentUsers
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api.resources import ordersResource


class IGetOrdersShipping(ABC):
    @abstractmethod
    def get_orders_shipping():
        pass


class OrdersShipping():
    def get_orders_shipping(self, request, UserId):
        if request.method == 'GET':
            users = shippingAgentUsers.objects.filter(UserId=UserId)
            if users.count() > 0:
                data = orders.objects.filter(
                    ShippingAgentId_id__in=[item.ShippingAgentId.id for item in users])
                Serializer = ordersResource(
                    data, many=True)
            return JsonResponse(Serializer.data, safe=False)


get_orders_shipping = OrdersShipping().get_orders_shipping
