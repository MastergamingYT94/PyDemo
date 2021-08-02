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
            if model == "inventoryDetails":
                checkExist = models.inventoryBalances.objects.filter(
                    ProductId=data["ProductId_id"], StoreId=data["StoreId_id"]).count()
                if checkExist == 0:
                    models.inventoryBalances.objects.create(
                        ProductId_id=data["ProductId_id"], StoreId_id=data["StoreId_id"], QuantityBalance=data["Quantity"])
                else:
                    quantityIn = models.inventoryDetails.objects.filter(
                        ProductId=data["ProductId_id"], StoreId=data["StoreId_id"]).aggregate(Sum('Quantity'))
                    models.inventoryBalances.objects.filter(
                        ProductId=data["ProductId_id"], StoreId=data["StoreId_id"]).update(QuantityBalance=quantityIn["Quantity__sum"])

            return HttpResponse(request)


add_data = addData().add
