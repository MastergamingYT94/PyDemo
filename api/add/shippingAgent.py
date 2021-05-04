from django.shortcuts import render
from PyCommerce.models import shippingAgent
from abc import ABC, abstractmethod


class IAddShippingAgent(ABC):
    @abstractmethod
    def shipping_agent():
        pass


class ShippingAgent():
    def shipping_agent(self, request):
        if request.method == "POST":
            saveRecord = shippingAgent()
            saveRecord.NameA = request.POST.get("NameA")
            saveRecord.NameL = request.POST.get("NameL")
            saveRecord.Adress1 = request.POST.get("Adress1")
            saveRecord.Adress2 = request.POST.get("Adress2")
            saveRecord.Phone = request.POST.get("Phone")
            saveRecord.Email = request.POST.get("Email")
            saveRecord.Password = request.POST.get("Password")
            saveRecord.PostCode = request.POST.get("PostCode")
            saveRecord.save()
        return render(request)


add_shipping_agent = ShippingAgent().shipping_agent
