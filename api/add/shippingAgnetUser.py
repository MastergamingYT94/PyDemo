from django.shortcuts import render
from PyCommerce.models import shippingAgentUser
from abc import ABC, abstractmethod


class IAddShippingAgentUser(ABC):
    @abstractmethod
    def shipping_agent_user():
        pass


class ShippingAgentUser():
    def shipping_agent_user(self, request):
        if request.method == "POST":
            saveRecord = shippingAgentUser()
            saveRecord.UserId = request.POST.get("UserId")
            saveRecord.ShippingAgentId = request.POST.get("ShippingAgentId")
            saveRecord.save()
        return render(request)


add_shipping_agent_user = ShippingAgentUser().shipping_agent_user
