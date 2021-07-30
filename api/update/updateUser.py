from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.http.response import HttpResponse
from PyCommerce.models import users
from api.encrypt import encrypt
import json


class IUpdateUser(ABC):
    @abstractmethod
    def update():
        pass


class updateUser():
    @csrf_exempt
    def update(self, request, id):
        if request.method == "POST":
            data = json.loads(request.body)
            password = data['Password']
            with open('key.json') as json_file:
                key = json.load(json_file)['key']
                token = encrypt(password, 'AES', key, False)
                data['Password'] = token['token']
            users.objects.filter(id=id).update(**data)
            return HttpResponse(request)


update_user = updateUser().update
