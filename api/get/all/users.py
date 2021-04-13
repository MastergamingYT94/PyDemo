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
            sanitizer = UsersResource(users.objects.all(), many=True)
            return JsonResponse(sanitizer.data, safe=False)


get_users = Users().users
