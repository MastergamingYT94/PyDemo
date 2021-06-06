import json
from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from PyCommerce.models import users


class IRegisterUser(ABC):
    @abstractmethod
    def register_user():
        pass


class RegisterUser():
    @csrf_exempt
    def register_user(self, request):
        if request.method == "POST":
            data = False
            result = json.loads(request.body)
            try:
                users.objects.filter(Email=result['Email'])
            except users.DoesNotExist:
                users.objects.create(**result)
                data = True
        return JsonResponse(data, safe=False)


register_user = RegisterUser().register_user
