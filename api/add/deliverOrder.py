from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from PyCommerce.models import orderMasters, orders


class IDeliverOrder(ABC):
    @abstractmethod
    def deliver_order():
        pass


class DeliverOrder():
    @csrf_exempt
    def deliver_order(self, request, OrderId, UserId):
        if request.method == "POST":
            Orders = orders.objects.filter(id=OrderId)
            Orders.update(isDelivered=True, DeliveredByUserId_id=UserId)
            count = orders.objects.filter(id=OrderId, MasterId__in=[
                                          item.MasterId.id for item in Orders]).count()
            delivered = orders.objects.filter(isDelivered=True).count()
            if (delivered / count) == 1:
                orderMasters.objects.filter(
                    id__in=[item.MasterId.id for item in Orders]).update(OrderStatusId_id=2)

        return JsonResponse(True, safe=False)


deliver_order = DeliverOrder().deliver_order
