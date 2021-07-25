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
        data = False
        if request.method == "POST":
            result = json.loads(request.body)
            Users = users.objects.filter(Email=result['Email'])
            if Users.count() > 0:
                data = False
            else:
                Serializer = users.objects.create(**result)
                data = {k: v for item in Serializer.data for k,
                        v in item.items()}
        return JsonResponse(data, safe=False)


register_user = RegisterUser().register_user
