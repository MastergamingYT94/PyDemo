from PyCommerce.models import orders, shippingAgentUsers
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api.resources import ordersResource


class IGetOrdersFiltered(ABC):
    @abstractmethod
    def get_orders_filtered():
        pass


class OrdersFiltered():
    def get_orders_filtered(self, request, UserId, Status=0):
        if request.method == 'GET':
            result = False
            users = shippingAgentUsers.objects.filter(UserId=UserId)
            Orders = orders.objects.filter(ShippingAgentId_id__in=[
                                           user.ShippingAgentId.id for user in users])
            if users.count() > 0:
                if Status == 0:
                    data = Orders
                if Status == 1:
                    data = Orders.filter(isDelivered=False)
                if Status == 2:
                    data = Orders.filter(isDelivered=True)
                result = ordersResource(data, many=True).data
        return JsonResponse(result, safe=False)


get_orders_filtered = OrdersFiltered().get_orders_filtered
