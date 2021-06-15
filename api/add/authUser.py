from api.resources import usersResource
from PyCommerce.models import users
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from django.views.decorators.csrf import csrf_exempt
import json


class IAuthenticateUser(ABC):
    @abstractmethod
    def authenticate_user():
        pass


class UserAuth():
    @csrf_exempt
    def authenticate_user(self, request):
        if request.method == 'POST':
            data = False
            result = json.loads(request.body)
            count = users.objects.filter(
                Email=result['Email'], Password=result['Password']).count()
            if count > 0:
                data = users.objects.filter(
                    Email=result['Email'], Password=result['Password'])
                Serializer = usersResource(data, many=True)
                data = {k: v for item in Serializer.data for k,
                        v in item.items()}
            return JsonResponse(data, safe=False)


authenticate_user = UserAuth().authenticate_user
