from django.db.models.base import Model
from PyCommerce import models
from django.http.response import JsonResponse
from abc import ABC, abstractmethod
from api import resources


class IGetAllData(ABC):
    @abstractmethod
    def all():
        pass


class AllData():
    def all(self, request, model):
        if request.method == 'GET':
            result = Model.__getattribute__(models, model)()
            resource = Model.__getattribute__(resources, model + 'Resource')()
            Serializer = resource(result.objects.all(), many=True)
            return JsonResponse(Serializer.data, safe=False)


get_all_data = AllData().all
