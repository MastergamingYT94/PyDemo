from django.shortcuts import render
from PyCommerce.models import shippingAgentUser
from abc import ABC, abstractmethod
from django.views.decorators.csrf import csrf_exempt


class IAddShippingAgentUser(ABC):
    @abstractmethod
    def shipping_agent_user():
        pass


class ShippingAgentUser():
    @csrf_exempt
    def shipping_agent_user(self, request):
        if request.method == "POST":
            result = shippingAgentUser()
            result.UserId = request.POST.get("UserId")
            result.ShippingAgentId = request.POST.get("ShippingAgentId")
            result.save()
            return render(request)


add_shipping_agent_user = ShippingAgentUser().shipping_agent_user
