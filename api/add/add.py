from django.db.models.aggregates import Sum
from django.views.decorators.csrf import csrf_exempt
from abc import ABC, abstractmethod
from django.http.response import HttpResponse
from PyCommerce import models
from django.db.models.base import Model
import json


class IAddData(ABC):
    @abstractmethod
    def add():
        pass


class addData():
    @csrf_exempt
    def add(self, request, model):
        if request.method == "POST":
            data = json.loads(request.body)
            result = Model.__getattribute__(models, model)()
            type(result).objects.create(**data)
            return HttpResponse(request)


add_data = addData().add
