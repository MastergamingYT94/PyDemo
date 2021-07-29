from api.encrypt import encrypt
from PyCommerce.models import users
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api.resources import usersResource


class IGetUser(ABC):
    @abstractmethod
    def get_user():
        pass


class User():
    def get_user(self, request, UserId):
        if request.method == 'GET':
            data = users.objects.filter(id=UserId)
            Serializer = usersResource(data, many=True)
            data = {k: v for item in Serializer.data for k,
                    v in item.items()}
            data = encrypt(data)
            return JsonResponse({'token': data['token'], 'key': data['key']}, safe=False)


get_user = User().get_user
