from abc import ABC, abstractmethod
from django.http.response import JsonResponse
from api.models import UsersResource
from PyCommerce.models import users


class IGetUser(ABC):
    @abstractmethod
    def user():
        pass


class User():
    def user(self, request, id):
        request.method = "GET"
        if request.method == 'GET':
            userSerializer = UsersResource(
                users.objects.filter(pk=id), many=True)
            return JsonResponse(userSerializer.data, safe=False)


get_user = User().user
