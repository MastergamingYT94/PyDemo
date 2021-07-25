from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from PyCommerce.models import cartTransactions


class IDeleteCart(ABC):
    @abstractmethod
    def delete_cart():
        pass


class DeleteCart():
    @csrf_exempt
    def delete_cart(self, request, cartId):
        if request.method == "DELETE":
            cartTransactions.objects.filter(MasterId=cartId).delete()
        return JsonResponse('Deleted Successfully', safe=False)


delete_cart = DeleteCart().delete_cart
