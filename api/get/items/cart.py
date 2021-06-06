from PyCommerce.models import cartTransactions
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api.resources import cartResource


class IGetCartItem(ABC):
    @abstractmethod
    def get_cart_item():
        pass


class CartItem():
    def get_cart_item(self, request, CartId):
        if request.method == 'GET':
            Serializer = False
            if CartId != 'null':
                data = cartTransactions.objects.filter(
                    MasterId=CartId)
                Serializer = cartResource(
                    data, many=True).data
            return JsonResponse(Serializer, safe=False)


get_cart_item = CartItem().get_cart_item
