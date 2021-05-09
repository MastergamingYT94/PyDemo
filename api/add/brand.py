from django.http.response import JsonResponse
from PyCommerce.models import brands
from abc import ABC, abstractmethod
from django.contrib import messages
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from api.models import BrandsResource


class IAddBrand(ABC):
    @abstractmethod
    def brand():
        pass


class Brand():
    @csrf_exempt
    def brand(self, request):
        print(request.method)

        if request.method == "POST":
            brand_Data = JSONParser().parse(request)
            brand_Serializer = BrandsResource(data=brand_Data)
            print(brand_Serializer)
            if brand_Serializer.is_valid():
                brand_Serializer.save()
                return JsonResponse("Saved Successfully", safe=False)


add_brand = Brand().brand
