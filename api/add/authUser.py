from PyCommerce.models import users
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from django.views.decorators.csrf import csrf_exempt
from api.resources import usersResource
from api.encrypt import encrypt
from api.decrypt import decrypt
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
                Email=result['Email']).values_list('Password', flat=True)
            for user in count:
                with open('key.json', "r") as json_file:
                    key = json.load(json_file)['key']
                    password = decrypt(user, key, 'RSA')
                    if result['Password'] == password:
                        data = users.objects.filter(Email=result['Email'])
                        Serializer = usersResource(data, many=True)
                        data = {k: v for item in Serializer.data for k,
                                v in item.items()}
            data = encrypt(data)
            return JsonResponse({'token': data['token'], 'key': data['key']}, safe=False)


authenticate_user = UserAuth().authenticate_user
