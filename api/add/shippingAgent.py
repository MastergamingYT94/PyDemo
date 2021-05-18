from django.shortcuts import render
from PyCommerce.models import shippingAgent
from abc import ABC, abstractmethod
from django.views.decorators.csrf import csrf_exempt


class IAddShippingAgent(ABC):
    @abstractmethod
    def shipping_agent():
        pass


class ShippingAgent():
    @csrf_exempt
    def shipping_agent(self, request):
        if request.method == "POST":
            result = shippingAgent()
            result.NameA = request.POST.get("NameA")
            result.NameL = request.POST.get("NameL")
            result.Adress1 = request.POST.get("Adress1")
            result.Adress2 = request.POST.get("Adress2")
            result.Phone = request.POST.get("Phone")
            result.Email = request.POST.get("Email")
            result.Password = request.POST.get("Password")
            result.PostCode = request.POST.get("PostCode")
            result.save()
            return render(request)


add_shipping_agent = ShippingAgent().shipping_agent
