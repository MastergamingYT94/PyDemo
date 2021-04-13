from django.http.response import JsonResponse
from PyCommerce.models import shippingAgentUser
from abc import ABC, abstractmethod


class IAddShippingAgentUser(ABC):
    @abstractmethod
    def shipping_agent_user():
        pass


class ShippingAgentUser():
    def shipping_agent_user(self, request):
        if request.method == "POST":
            get = request.POST.get

            shippingAgentUser.objects.create(
                UserId=get('UserId'),
                ShippingAgentId=get('ShippingAgentId'))
            return JsonResponse(request.POST, safe=False)


add_shipping_agent_user = ShippingAgentUser().shipping_agent_user
