from django.db import models
from django.db.models.base import Model
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api import resources


class IGetData(ABC):
    @abstractmethod
    def data():
        pass


class Data():
    def data(self, request, model, id):
        if request.method == 'GET':
            result = Model.__getattribute__(models, model)()
            resource = Model.__getattribute__(resources, model + 'Resource')
            Serializer = resource(type(result).objects.get(id=id), many=True)
            return JsonResponse(Serializer.data, safe=False)


get_data = Data().data
