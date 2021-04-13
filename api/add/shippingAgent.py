from django.http.response import JsonResponse
from PyCommerce.models import shippingAgent
from abc import ABC, abstractmethod


class IAddShippingAgent(ABC):
    @abstractmethod
    def shipping_agent():
        pass


class ShippingAgent():
    def shipping_agent(self, request):
        if request.method == "POST":
            get = request.POST.get

            shippingAgent.objects.create(
                NameA=get('NameA'),
                NameL=get('NameL'),
                Adress1=get('Adress1'),
                Adress2=get('Adress2'),
                Phone=get('Phone'),
                Email=get('Email'),
                Password=get('Password'),
                PostCode=get('PostCode')
            )
            return JsonResponse(request.POST, safe=False)


add_shipping_agent = ShippingAgent().shipping_agent
