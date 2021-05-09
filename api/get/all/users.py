from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import UsersResource
from PyCommerce.models import users


class IGetUsers(ABC):
    @abstractmethod
    def users():
        pass


class Users():
    def users(self, request):
        if request.method == 'GET':
            usersSerializer = UsersResource(users.objects.all(), many=True)
            return JsonResponse(usersSerializer.data, safe=False)


get_users = Users().users
