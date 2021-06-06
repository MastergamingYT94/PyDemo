from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.http.response import HttpResponse
from PyCommerce import models
from django.db.models.base import Model
import json


class IUpdateData(ABC):
    @abstractmethod
    def update():
        pass


class updateData():
    @csrf_exempt
    def update(self, request, model, id):
        if request.method == "POST":
            data = json.loads(request.body)
            result = Model.__getattribute__(models, model)()
            type(result).objects.filter(id=id).update(**data)
            return HttpResponse(request)


update_data = updateData().update
