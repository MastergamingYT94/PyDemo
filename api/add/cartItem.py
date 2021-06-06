import json
from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from PyCommerce.models import cartTransactions, products


class IAddCartItem(ABC):
    @abstractmethod
    def add_cart_item():
        pass


class CartItem():
    @csrf_exempt
    def add_cart_item(self, request):
        if request.method == "POST":
            result = json.loads(request.body)
            items = cartTransactions.objects.filter(
                ProductId=result['ProductId'], StoreId=result['StoreId'], MasterId=result['MasterId'])
            count = items.count()
            result['Quantity'] = 1
            if count > 0:
                items = [item for item in items]
                for item in items:
                    result['Quantity'] = item.Quantity + result['Quantity']
                    cartTransactions.objects.filter(id=item.id).update(
                        Quantity=result['Quantity'], ProductId_id=result['ProductId'], MasterId_id=result['MasterId'], StoreId_id=result['StoreId'], IsOrdered=False)
            else:
                cartTransactions.objects.create(
                    Quantity=result['Quantity'], ProductId_id=result['ProductId'], MasterId_id=result['MasterId'], StoreId_id=result['StoreId'], IsOrdered=False)

            return JsonResponse(result)


add_cart_item = CartItem().add_cart_item
