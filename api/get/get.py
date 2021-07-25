from django.db.models.base import Model
from django.http.response import JsonResponse
from PyCommerce import models
from abc import ABC, abstractmethod
from api import resources
from api.encrypt import Encrypt


class IGetData(ABC):
    @abstractmethod
    def data():
        pass


class Data():
    def data(self, request, model, id):
        if request.method == 'GET':
            result = Model.__getattribute__(models, model)()
            resource = Model.__getattribute__(resources, model + 'Resource')
            Serializer = resource(
                type(result).objects.filter(id=id), many=True)
            data = {k: v for item in Serializer.data for k,
                    v in item.items()}
            data = Encrypt().encrypt(data)
            return JsonResponse({'token': data['token'], 'key': data['key']}, safe=False)


get_data = Data().data
