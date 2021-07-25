from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from PyCommerce.models import cartTransactions


class IDeleteCartItem(ABC):
    @abstractmethod
    def delete_cart_item():
        pass


class DeleteCartItem():
    @csrf_exempt
    def delete_cart_item(self, request, id):
        if request.method == "DELETE":
            cartTransactions.objects.filter(id=id).delete()
        return JsonResponse('Deleted Successfully', safe=False)


delete_cart_item = DeleteCartItem().delete_cart_item
