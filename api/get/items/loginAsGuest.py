from PyCommerce.models import users
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api.resources import usersResource


class ILoginAsGuest(ABC):
    @abstractmethod
    def login_as_guest():
        pass


class LoginAsGuest():
    def login_as_guest(self, request):
        if request.method == 'GET':
            data = users.objects.filter(NameL='Guest')
            Serializer = usersResource(data, many=True)
            data = {k: v for item in Serializer.data for k,
                    v in item.items()}
            return JsonResponse(data, safe=False)


login_as_guest = LoginAsGuest().login_as_guest
