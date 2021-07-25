import json
from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from PyCommerce.models import orderMasters, orders, shippingAgentUsers, shippingDetails


class IDeliveryNotes(ABC):
    @abstractmethod
    def add_delivery_notes():
        pass


class DeliveryNotes():
    @csrf_exempt
    def add_delivery_notes(self, request, OrderId, UserId):
        if request.method == "POST":
            data = json.loads(request.body)
            users = shippingAgentUsers.objects.filter(
                UserId=UserId)
            master = [
                item.MasterId.id for item in orders.objects.filter(id=OrderId)]
            if users.count() > 0:
                for agent in [item.ShippingAgentId.id for item in users]:
                    agent
                shippingDetails.objects.create(
                    ShippingAgentId_id=agent, OrderId_id=OrderId, DeliveryNotes=data['Notes'])
                orders.objects.filter(id=OrderId).update(
                    Longitude=data['Longitude'], Latitude=data['Latitude'])
                orderMasters.objects.filter(
                    id__in=master).update(OrderStatusId_id=1)
            return JsonResponse(data.id, safe=False)


add_delivery_notes = DeliveryNotes().add_delivery_notes
