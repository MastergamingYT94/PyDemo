from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from PyCommerce.models import cartTransactions


class IUpdateCartQuantity(ABC):
    @abstractmethod
    def update_cart_quantity():
        pass


class CartQuantity():
    @csrf_exempt
    def update_cart_quantity(self, request, cartId, Quantity):
        if request.method == "POST":
            data = cartTransactions.objects.filter(
                id=cartId).update(Quantity=Quantity)
            return JsonResponse(data, safe=False)


update_cart_quantity = CartQuantity().update_cart_quantity
