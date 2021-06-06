import json
from PyCommerce.models import inventoryBalances
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api.resources import cartItemsResource


class IGetCartItem(ABC):
    @abstractmethod
    def get_cart_item():
        pass


class CartItem():
    def get_cart_item(self, request, ProductId=None):
        if request.method == 'GET':
            data = inventoryBalances.objects.filter(
                id=ProductId)
            Serializer = cartItemsResource(
                data, many=True)
            data = {k: v for item in Serializer.data for k,
                    v in item.items()}
            return JsonResponse(data, safe=False)


get_cart_item = CartItem().get_cart_item
